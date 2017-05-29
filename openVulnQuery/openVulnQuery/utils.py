import sys
import csv
import json

import constants


def filter_advisories(advisories, fields):
    filtered_list = []
    is_nested_ips_signature_field = any(field in constants.IPS_SIGNATURES for field in fields)
    if is_nested_ips_signature_field:
        fields.append('ips_signatures')
    if 'ips_signatures' in fields and not is_nested_ips_signature_field:
        fields.extend(constants.IPS_SIGNATURES)
    for advisory in advisories:
        filtered_list.append(advisory.filter(*fields))
    return filtered_list


def count_fields(advisories, fields):

    counts = dict.fromkeys(fields, 0)
    for advisory in advisories:
        for field in fields:
            if hasattr(advisory, field):
                counts[field] += get_count(getattr(advisory, field))
    return counts


def get_count(advisory_field):
    """Returns a count of the number of valid items in a particular advisory field"""

    count = 0
    if isinstance(advisory_field, (str, unicode)):
        if advisory_field != 'NA':
            count = 1
    else:
        for item in advisory_field:
            if item != 'NA':
                count += 1
    return count


def output(advisories, output_format, file_handle):
    """Display data in different formats (CSV, JSON, Pretty Printed Table).

    Args:
        advisories: List of advisory objects.
        output_format: Either set as csv or json or use default stdout.
        file_handle: The path to put the csv or json file with a file name or stdout if no path or filename.

    Returns:
        Output displayed in format (CSV, JSON, Pretty Printed Table).

    """
    if output_format == 'json':
        _to_json(advisories, file_handle)
    elif output_format == 'csv':
        _to_csv(advisories, file_handle, delimiter=",")


def _to_json(advisory_list, file_handle):
    """Write json to a file"""

    json_data = json.dumps(advisory_list, sort_keys=True, indent=4)
    file_handle.write(json_data)


def _to_csv(advisory_list, file_handle, delimiter):
    """Write csv to a file, with option to specify a delimiter"""

    flattened_advisory_list = flatten_list(advisory_list)

    header = flattened_advisory_list[0].keys()

    w = csv.DictWriter(file_handle, header, delimiter=delimiter, extrasaction='ignore', restval='NA')
    w.writeheader()

    for advisory in flattened_advisory_list:
        w.writerow(advisory)


def flatten_list(advisory_list):
    adv_list = []
    for advisory in advisory_list:
        adv_list.append(_flatten_datastructure(advisory))
    return adv_list


def _flatten_datastructure(field_list):
    final_dict = {}
    for k, v in field_list.iteritems():
        if isinstance(v, list):
            if v and isinstance(v[0], dict):
                final_dict.update(_reduce_list_dict(k, v))
            else:
                final_dict[k] = u'\t'.join(v)
        else:
            final_dict[k] = v.encode('utf-8').strip() if v else None
    return final_dict


def _reduce_list_dict(node, vals):
    keys = vals[0].keys()
    flattened_dict = {"%s_%s" % (node, k): "" for k in keys}
    for v in vals:
        for key in keys:
            flattened_key = "%s_%s" % (node, key)
            upd_val = "%s\t%s" % (flattened_dict[flattened_key], v[key])
            flattened_dict[flattened_key] = upd_val
    return flattened_dict


def get_output_filehandle(file_path=None):
    """Returns file handle if file_path given else returns stdout handle"""

    return open(file_path, "w") if file_path else sys.stdout

