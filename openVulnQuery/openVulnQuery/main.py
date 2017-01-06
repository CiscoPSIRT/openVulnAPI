import argparse
import datetime

import config
import query_client
import utils

# need to update this list if you add new fields to the advisory
API_LABELS = ['advisory_id', 'sir', 'first_published', 'last_updated', 'cves', 'cvss_base_score',
              'advisory_title', 'publication_url', 'cwe', 'product_names', 'summary',
              'oval_url', 'cvrf_url', 'bug_ids']
allows_filter = ['all', 'severity']


def process_command_line():
    """Interpret parameters in command line"""

    parser = argparse.ArgumentParser(description='Cisco OpenVuln API Command Line Interface')
    parser.set_defaults(output_format=('stdout', None))

    advisory_format = parser.add_mutually_exclusive_group(required=True)
    api_resource = parser.add_mutually_exclusive_group(required=True)
    output_format = parser.add_mutually_exclusive_group()
    additional_filter = parser.add_mutually_exclusive_group()

    advisory_format.add_argument('--cvrf',
                                 action='store_const',
                                 const='cvrf',
                                 dest='advisory_format',
                                 help='Selects from cvrf advisories')
    advisory_format.add_argument('--oval',
                                 action='store_const',
                                 const='oval',
                                 dest='advisory_format',
                                 help='Selects from oval advisories')

    api_resource.add_argument('--all',
                              action='store_const',
                              const=('all', 'all'),
                              dest='api_resource',
                              help='Retrieve all cvrf/oval advisiories')
    api_resource.add_argument('--advisory',
                              dest='api_resource',
                              type=(lambda x: ('advisory', x)),
                              help='Retrieve advisories by advisory id')
    api_resource.add_argument('--cve',
                              dest='api_resource',
                              type=(lambda x: ('cve', x)),
                              help='Retrieve advisories by cve id')
    api_resource.add_argument('--latest',
                              dest='api_resource',
                              type=(lambda x: ('latest', x)),
                              help='Retrieve latest (number) of advisories')
    api_resource.add_argument('--severity',
                              dest='api_resource',
                              type=(lambda x: ('severity', x)),
                              help='Retrieve advisories by severity (low, medium, high, critical)')
    api_resource.add_argument('--year',
                              dest='api_resource',
                              type=(lambda x: ('year', x)),
                              help='Retrieve advisories by year')

    api_resource.add_argument('--product',
                              dest='api_resource',
                              type=(lambda x: ('product', x)),
                              help='Retrieve advisories by product names')
    api_resource.add_argument('--ios_xe',
                              dest='api_resource',
                              type=(lambda x: ('ios_xe', x)),
                              help='Retrieve advisories affecting user inputted iso_xe version.'
                                   'Only one version at a time is allowed.')

    output_format.add_argument('--csv',
                               dest='output_format',
                               type=(lambda x: ('csv', x)),
                               help='Output to CSV with file path')
    output_format.add_argument('--json',
                               dest='output_format',
                               type=(lambda x: ('json', x)),
                               help='Output to JSON with file path')
    additional_filter.add_argument('--first_published',
                                   dest='first_published',
                                   type=valid_date,
                                   help='Filter advisories based on first_published date YYYY-MM-DD:YYYY-MM-DD')
    additional_filter.add_argument('--last_updated',
                                   dest='last_updated',
                                   type=valid_date,
                                   help='Filter advisories based on last_updated date YYYY-MM-DD:YYYY-MM-DD')

    parser.add_argument('--count', '-c',
                        action='store_true',
                        help='Count of any field or fields')
    parser.add_argument('--fields', '-f',
                        dest='fields',
                        nargs='+',
                        choices=API_LABELS,
                        help='Separate fields by spaces to return advisory information')

    return parser.parse_args()


def valid_date(date_text):
    try:
        start_date, end_date = date_text.split(':')
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
        return start_date, end_date
    except ValueError:
        raise argparse.ArgumentTypeError('%s not a valid date. Enter date in YYYY-MM-DD format')


def main():

    args = process_command_line()
    api_resource_key, api_resource_value = args.api_resource

    client = query_client.OpenVulnQueryClient(config.TEST_ClIENT_ID, config.TEST_CLIENT_SECRET)
    query_client_func = getattr(client, 'get_by_{0}'.format(api_resource_key))

    if not args.fields:
        if args.advisory_format == 'cvrf':
            API_LABELS.remove('oval_url')
        else:
            API_LABELS.remove('cvrf_url')
        args.fields = API_LABELS
    if api_resource_key in allows_filter:
        filter = query_client.Filter()
        if args.first_published:
            start_date, end_date = args.first_published
            filter = query_client.FirstPublishedFilter(start_date, end_date)
        elif args.last_updated:
            start_date, end_date = args.last_updated
            filter = query_client.LastPublishedFilter(start_date, end_date)
        advisories = query_client_func(args.advisory_format, api_resource_value, filter)
    else:
        advisories = query_client_func(args.advisory_format, api_resource_value)

    returned_output = None
    if(args.count):
        returned_output = [utils.count_fields(advisories, args.fields)]
    else:
        returned_output = utils.filter_advisories(advisories, args.fields)

    output_format, file_path = args.output_format
    if not args.fields:
        output_format = 'json'
    with utils.get_output_filehandle(file_path) as f:
        utils.output(returned_output, output_format, f)


if __name__ == '__main__':
    main()
