import csv
import json
import sys

from . import constants
from ._compatibility import is_unicode_or_bytes

TAB = u'\t'
IPS_SIG = constants.IPS_SIGNATURE_LABEL


def filter_advisories(advisories, fields):
    """Filter the advisories per some criteria ...

    :param advisories: An iterable with advisory entries
    :param fields: The requested fields (TODO reverse documentation?)
    :return list of advisories passing filter criteria
    """
    is_nested_ips_signature_field = any(
        field in constants.IPS_SIGNATURES for field in fields)

    filter_fields = list(fields)
    if is_nested_ips_signature_field:
        filter_fields.append(IPS_SIG)
    elif IPS_SIG in fields:  # and not is_nested_ips_signature_field:
        filter_fields.extend(constants.IPS_SIGNATURES)

    return [adv.filter(*filter_fields) for adv in advisories]


def count_fields(advisories, fields):
    """Counter dict from fields over all advisories. """
    counts = dict.fromkeys(fields, 0)
    for adv in advisories:
        for field in fields:
            if hasattr(adv, field):
                counts[field] += get_count(getattr(adv, field))
    return counts


def get_count(advisory_field):
    """Count of the number of valid items in a particular advisory field."""

    count = 0
    if is_unicode_or_bytes(advisory_field):
        if advisory_field != constants.NA_INDICATOR:
            count = 1
    else:
        for item in advisory_field:
            if item != constants.NA_INDICATOR:
                count += 1
    return count


def output(advisories, output_format, file_handle):
    """Write data in CSV or JSON to file_handle .

    :param advisories: List of advisory objects.
    :param output_format: Either set as csv or json or use default stdout.
    :param file_handle: The path to put the csv or json file with a file name
        or stdout if no path or filename.
    """
    if output_format == constants.JSON_OUTPUT_FORMAT_TOKEN:
        _to_json(advisories, file_handle)
    elif output_format == constants.CSV_OUTPUT_FORMAT_TOKEN:
        _to_csv(advisories, file_handle, delimiter=",")


def _to_json(advisory_list, file_handle):
    """Write json to a file"""
    file_handle.write(json.dumps(advisory_list, sort_keys=True, indent=4))


def _to_csv(advisory_list, file_handle, delimiter):
    """Write csv to a file, with option to specify a delimiter"""

    flattened_advisory_list = flatten_list(advisory_list)
    header = _get_headers(flattened_advisory_list)
    if IPS_SIG in header:
        header.remove(IPS_SIG)

    w = csv.DictWriter(file_handle, header, delimiter=delimiter,
                       extrasaction='ignore', restval=constants.NA_INDICATOR)
    w.writeheader()
    for advisory in flattened_advisory_list:
        w.writerow(advisory)


def flatten_list(advisory_seq):
    """Flatten the structures returned as list."""
    return [_flatten_datastructure(adv) for adv in advisory_seq]


def _get_headers(advisories):
    """Return list of unique headers."""
    return list(set(key for adv in advisories for key in adv.keys()))


def _flatten_datastructure(field_list):
    final_dict = {}
    for k, v in field_list.items():
        if isinstance(v, list):
            if v and isinstance(v[0], dict):
                final_dict.update(_reduce_list_dict(k, v))
            else:
                final_dict[k] = TAB.join(v)
        else:
            final_dict[k] = v.encode('utf-8').strip() if v else None
    return final_dict


def _reduce_list_dict(node, vals):
    keys = vals[0].keys()
    flattened_dict = {"%s_%s" % (node, k): "" for k in keys}
    for v in vals:
        for key in keys:
            separator = ""
            flattened_key = "%s_%s" % (node, key)
            if flattened_dict[flattened_key] != "":
                separator = "\t"
            upd_val = (
                "%s%s%s" % (flattened_dict[flattened_key], separator, v[key]))
            flattened_dict[flattened_key] = upd_val
    return flattened_dict


def get_output_filehandle(file_path=None):
    """File handle if file_path given else returns stdout handle"""
    return open(file_path, "w") if file_path else sys.stdout
