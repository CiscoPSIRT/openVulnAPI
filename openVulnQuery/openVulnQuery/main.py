import argparse
import config
import csv
import json
import logging
import query_client
import sys
from collections import defaultdict
from prettytable import PrettyTable

API_LABELS = ['sir', 'last_updated', 'first_published', 'advisory_id', 'cves', 'cvrf_url', 'oval_urls']
CVRF_LABELS = ['document_title', 'summary', 'publication_url', 'full_product_name_list']
VULN_LABELS = ['vuln_title', 'vuln_base_score', 'vuln_bug_ids', 'vuln_cve']
PRINT_OUT = sys.stdout

def process_command_line():
    """Interpret parameters in command line"""

    parser = argparse.ArgumentParser(description = 'Cisco OpenVuln API Command Line Interface')
    parser.set_defaults(output_format=('stdout', None))

    advisory_format = parser.add_mutually_exclusive_group(required=True)
    api_resource = parser.add_mutually_exclusive_group(required=True)
    output_format = parser.add_mutually_exclusive_group()

    advisory_format.add_argument('--cvrf',
                                 action='store_const',
                                 const='cvrf',
                                 dest='advisory_format',
                                 help='Filter by cvrf advisories')
    advisory_format.add_argument('--oval',
                                 action='store_const',
                                 const='oval',
                                 dest='advisory_format',
                                 help='Filter by oval advisories')

    api_resource.add_argument('--all',
                         action='store_const',
                         const=('all', 'all'),
                         dest='api_resource',
                         help='Get all cvrf/oval advisiories')
    api_resource.add_argument('--advisory',
                         dest='api_resource',
                         type=(lambda x: ('advisory', x)),
                         help='Search advisories by advisory id')
    api_resource.add_argument('--cve',
                         dest='api_resource',
                         type=(lambda x: ('cve', x)),
                         help='Search advisories by cve id')
    api_resource.add_argument('--latest',
                         dest='api_resource',
                         type=(lambda x: ('latest', x)),
                         help='Show latest (number) of advisories')
    api_resource.add_argument('--severity',
                         dest='api_resource',
                         type=(lambda x: ('severity', x)),
                         help='Filter advisories by severity (low, medium, high, critical)')
    api_resource.add_argument('--year',
                         dest='api_resource',
                         type=(lambda x: ('year', x)),
                         help='Filter advisories by year')

    output_format.add_argument('--csv',
                               dest='output_format',
                               type=(lambda x: ('csv', x)),
                               help='Output to CSV with filepath')
    output_format.add_argument('--json',
                               dest='output_format',
                               type=(lambda x: ('json', x)),
                               help='Output to JSON with filepath')

    parser.add_argument('--count', '-c',
                        action='store_true',
                        help='Count of any field or fields')
    parser.add_argument('--fields', '-f',
                        dest='entered_fields',
                        nargs='+',
                        help='Seperate fields by spaces to return advisory information')
    parser.add_argument('--show_fields',
                        action='store_true',
                        help='Display all of the fields for use in -f or --fields')

    return parser.parse_args()

def parse_advisory_objects(advisories, api_fields, cvrf_fields, vuln_fields):
    """Take advisory object and convert it to a list of dictionaries and count requested fields

    Args:
        advisories: List of advisory objects.
        api_fields: User input of fields requested from API
        cvrf_fields: User input of fields requested from CVRF_XML
        vuln_fields: User input of fields requested from CVRF_XML Vulnerability(s)

    Returns:
        List of parsed advisories and a dictionary of fields and their respective counts.

    """
    combined_fields = api_fields + cvrf_fields
    advs = []
    fields_counted_dict = defaultdict(int)

    for adv in advisories:
        adv_data = {}
        if combined_fields:
            for field in combined_fields:
                if field in api_fields:
                    obj = adv
                elif field in cvrf_fields:
                    obj = adv.cvrf

                adv_data[field] = getattr(obj, field)
                fields_counted_dict[field] += count_field(adv_data[field])

        if vuln_fields:
            adv_data['vulns'] = []
            for vuln in adv.cvrf.vuln_list:
                vuln_info = {}
                for field in vuln_fields:
                    vuln_info[field] = getattr(vuln, field)
                    fields_counted_dict[field] += count_field(vuln_info[field])
                adv_data['vulns'].append(vuln_info)

        advs.append(adv_data)
    return fields_counted_dict, advs

def count_field(advisory_field):
    """Returns a count of the number of valid items in a particular advisory field"""

    count = 0
    if isinstance(advisory_field, (str, unicode)):
        if advisory_field != 'NA':
            count=1
    else:
        for item in advisory_field:
            if item != 'NA':
                count+=1
    return count

def output(advisory_list, output_format, file_handle):
    """Display data in different formats (CSV, JSON, Pretty Printed Table).

    Args:
        advisory_list: List of advisory objects.
        output_format: Either set as csv or json or use default stdout.
        file_handle: The path to put the csv or json file with a file name or stdout if no path or filename.

    Returns:
        Output displayed in format (CSV, JSON, Pretty Printed Table).

    """
    if output_format == 'json':
         _json_to_file(advisory_list, file_handle)
    elif output_format == 'csv':
        _csv_to_file(map_vulnerabilites_to_advisory(advisory_list), file_handle, delimiter = ",")
    else:
        _stdout_table(map_vulnerabilites_to_advisory(advisory_list))

def _json_to_file(advisory_list, file_handle):
    """Write json to a file"""

    json_data = json.dumps(advisory_list, sort_keys = True, indent = 4)
    file_handle.write(json_data)

def _stdout_table(advisory_list):
    """Display data in pretty printed tabular format"""

    header = advisory_list[0].keys()
    table = PrettyTable(header)

    for advisory in advisory_list:
        row = _convert_list_to_string(advisory)
        table.add_row(row.values())
    print(table)

def _csv_to_file(advisory_list, file_handle, delimiter):
    """Write csv to a file, with option to specify a delimeter"""

    header = advisory_list[0].keys()
    w = csv.DictWriter(file_handle, header)
    w.writeheader()

    for advisory in advisory_list:
        w.writerow(_convert_list_to_string(advisory))

def _convert_list_to_string(field_list):
    """Converts dictionary values that are list to string seperated by space"""

    return {k: '    '.join(v) if isinstance(v, list) else v
            for k,v in field_list.items()}

def map_vulnerabilites_to_advisory(advisories):
    """Creates a copy of an advisory depending on the number of vulnerabilities to link each vulnerability with its advisory one per line in table or csv format"""

    updated_advisories = []
    for advisory_dict in advisories:
        if 'vulns' in advisory_dict:
            for vuln in advisory_dict['vulns']:
                for key, val in vuln.items():
                    advisory_dict.pop('vulns', None)
                    advisory_dict[key] = val
                    updated_advisories.append(advisory_dict.copy())
        else:
            updated_advisories.append(advisory_dict)
    return updated_advisories

def filter_entered_fields(entered_fields):
    """Take user entered fields and convert them to the specific group for parsing Advisory object"""

    api_fields = [x for x in entered_fields if x in API_LABELS]
    cvrf_fields = [x for x in entered_fields if x in CVRF_LABELS]
    vuln_fields = [x for x in entered_fields if x in VULN_LABELS]

    return api_fields, cvrf_fields, vuln_fields

def xml_parse_needed(adv_format, entered_fields):
    """Determines whether cvrf xml file needs to be parsed for fields based off user entry"""

    xml_labels = CVRF_LABELS + VULN_LABELS
    for x in entered_fields:
        if x in xml_labels and adv_format != 'oval':
            return True
    return False

def get_output_filehandle(file_path=None):
    """Returns filehandle if file_path given else returns stdout handle"""

    return open(file_path, "w") if file_path else PRINT_OUT;

def main():
    """Process input, get auth_token, filter fields, and display results."""

    args = process_command_line()

    if args.show_fields:
        fields = API_LABELS + CVRF_LABELS + VULN_LABELS
        PRINT_OUT.write("\n".join(fields))
    else:
        api_resource_key, api_resource_value = args.api_resource

        client = query_client.OpenVulnQueryClient(config.CLIENT_ID, config.CLIENT_SECRET)
        call_query_client_func = getattr(client, "get_by_{0}".format(api_resource_key))

        if not args.entered_fields:
            if args.advisory_format == 'cvrf':
                API_LABELS.remove('oval_urls')
            else:
                API_LABELS.remove('cvrf_url')
            args.entered_fields = API_LABELS

        parse_xml = xml_parse_needed(args.advisory_format, args.entered_fields)
        advisory_objects = call_query_client_func(args.advisory_format, api_resource_value, parse_xml)

        api_fields, cvrf_fields, vuln_fields = filter_entered_fields(args.entered_fields)
        count_dict, parsed_advisories = parse_advisory_objects(advisory_objects, api_fields, cvrf_fields, vuln_fields)

        if args.count:
            for field, count in count_dict.iteritems():
                PRINT_OUT.write(field + " : " + str(count) + "\n")
        else:
            output_format, file_path = args.output_format
            if not args.entered_fields:
                output_format = 'json'

            with get_output_filehandle(file_path) as f:
                output(parsed_advisories, output_format, f)

if __name__ == '__main__':
    main()
