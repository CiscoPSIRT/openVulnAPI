import sys
from prettytable import PrettyTable
import csv
import json


def filter_advisories(advisories, fields):
    filtered_list = []
    for advisory in advisories:
        filtered_list.append(advisory.filter(*fields))
    return filtered_list


def count_fields(advisories, fields):

    counts = dict.fromkeys(fields, 0)
    for advisory in advisories:
        for field in fields:
            if hasattr(advisory, field):
                counts[field] += count_field(getattr(advisory, field))
    return counts


def count_field(advisory_field):
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
    else:
        _to_stdout(advisories)


def _to_json(advisory_list, file_handle):
    """Write json to a file"""

    json_data = json.dumps(advisory_list, sort_keys=True, indent=4)
    file_handle.write(json_data)


def _to_stdout(advisories):
    """Display data in pretty printed tabular format"""

    header = advisories[0].keys()
    table = PrettyTable(header)

    for advisory in advisories:
        row = _convert_list_to_string(advisory)
        table.add_row(row.values())
    print(table)


def _to_csv(advisory_list, file_handle, delimiter):
    """Write csv to a file, with option to specify a delimiter"""

    header = advisory_list[0].keys()
    w = csv.DictWriter(file_handle, header, delimiter=delimiter)
    w.writeheader()

    for advisory in advisory_list:
        w.writerow(_convert_list_to_string(advisory))


def _convert_list_to_string(field_list):
    """Converts dictionary values that are list to string separated by space"""

    return {k: '\t'.join(v) if isinstance(v, list) else v
            for k, v in field_list.items()}


def get_output_filehandle(file_path=None):
    """Returns file handle if file_path given else returns stdout handle"""

    return open(file_path, "w") if file_path else sys.stdout;
