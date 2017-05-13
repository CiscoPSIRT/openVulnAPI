import argparse
import datetime

import config
import constants
import query_client
import utils


def process_command_line():
    """Interpret parameters in command line"""

    parser = argparse.ArgumentParser(prog='openVulnQuery', description='Cisco OpenVuln API Command Line Interface')
    parser.set_defaults(output_format=('json', None))

    advisory_format = parser.add_mutually_exclusive_group(required=False)
    api_resource = parser.add_mutually_exclusive_group(required=True)
    output_format = parser.add_mutually_exclusive_group()
    additional_filter = parser.add_mutually_exclusive_group()

    advisory_format.add_argument('--cvrf',
                                 action='store_const',
                                 const='cvrf',
                                 dest='advisory_format',
                                 help='Selects from cvrf advisories, required except for ios and ios_xe query')
    advisory_format.add_argument('--oval',
                                 action='store_const',
                                 const='oval',
                                 dest='advisory_format',
                                 help='Selects from oval advisories, required except for ios and ios_xe query')

    api_resource.add_argument('--all',
                              action='store_const',
                              const=('all', 'all'),
                              dest='api_resource',
                              help='Retrieve all cvrf/oval advisiories')
    api_resource.add_argument('--advisory',
                              dest='api_resource',
                              metavar='<advisory-id>',
                              type=(lambda x: ('advisory', x)),
                              help='Retrieve advisories by advisory id')
    api_resource.add_argument('--cve',
                              dest='api_resource',
                              metavar='<CVE-id>',
                              type=(lambda x: ('cve', x)),
                              help='Retrieve advisories by cve id')
    api_resource.add_argument('--latest',
                              dest='api_resource',
                              metavar='number',
                              type=(lambda x: ('latest', x)),
                              help='Retrieve latest (number) of advisories')
    api_resource.add_argument('--severity',
                              dest='api_resource',
                              metavar='[critical, high, medium, low]',
                              type=(lambda x: ('severity', x)),
                              help='Retrieve advisories by severity (low, medium, high, critical)')
    api_resource.add_argument('--year',
                              dest='api_resource',
                              metavar='year',
                              type=(lambda x: ('year', x)),
                              help='Retrieve advisories by year')

    api_resource.add_argument('--product',
                              dest='api_resource',
                              metavar='product_name',
                              type=(lambda x: ('product', x)),
                              help='Retrieve advisories by product names')
    api_resource.add_argument('--ios_xe',
                              dest='api_resource',
                              metavar='iosxe_version',
                              type=(lambda x: ('ios_xe', x)),
                              help='Retrieve advisories affecting user inputted iso_xe version.'
                                   'Only one version at a time is allowed.')
    api_resource.add_argument('--ios',
                              dest='api_resource',
                              metavar='ios_version',
                              type=(lambda x: ('ios', x)),
                              help='Retrieve advisories affecting user inputted iso version.'
                                   'Only one version at a time is allowed.')
    output_format.add_argument('--csv',
                               dest='output_format',
                               metavar='filepath',
                               type=(lambda x: ('csv', x)),
                               help='Output to CSV with file path')
    output_format.add_argument('--json',
                               dest='output_format',
                               metavar='filepath',
                               type=(lambda x: ('json', x)),
                               help='Output to JSON with file path')
    additional_filter.add_argument('--first_published',
                                   dest='first_published',
                                   metavar='YYYY-MM-DD:YYYY-MM-DD',
                                   type=valid_date,
                                   help='Filter advisories based on first_published date YYYY-MM-DD:YYYY-MM-DD'
                                        ' USAGE: followed by severity or all')
    additional_filter.add_argument('--last_published',
                                   dest='last_published',
                                   metavar='YYYY-MM-DD:YYYY-MM-DD',
                                   type=valid_date,
                                   help='Filter advisories based on last_published date YYYY-MM-DD:YYYY-MM-DD'
                                        ' USAGE: followed by severity or all')

    parser.add_argument('--count', '-c',
                        action='store_true',
                        help='Count of any field or fields')
    parser.add_argument('--fields', '-f',
                        dest='fields',
                        nargs='+',
                        metavar='',
                        choices=constants.API_LABELS + constants.IPS_SIGNATURES,
                        help='Separate fields by spaces to return advisory information. Allowed values are: %s' % ', '.join(constants.API_LABELS))

    args = parser.parse_args()
    if not args.advisory_format:
        key, val = args.api_resource
        if key not in ['ios', 'ios_xe']:
            parser.error('Advisory format --cvrf or --oval required except for ios and ios_xe')

    if args.api_resource[0] not in constants.allows_filter:
        if args.first_published or args.last_published:
            parser.error('Only %s based filter can have additional first_published or last_published filter' % constants.allows_filter)
    return args


def valid_date(date_text):
    try:
        start_date, end_date = date_text.split(':')
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if start_date_obj > end_date_obj:
            raise argparse.ArgumentTypeError('StartDate(%s) should me smaller than EndDate(%s)' % (start_date, end_date))
        if start_date_obj > datetime.datetime.now() or end_date_obj > datetime.datetime.now():
            raise argparse.ArgumentTypeError('Invalid date %s' % date_text)
        return start_date, end_date
    except ValueError:
        raise argparse.ArgumentTypeError('%s is not a valid date format. Enter date in YYYY-MM-DD:YYYY-MM-DD format' % date_text)


def main():

    args = process_command_line()
    api_resource_key, api_resource_value = args.api_resource

    client = query_client.OpenVulnQueryClient(config.CLIENT_ID, config.CLIENT_SECRET)
    query_client_func = getattr(client, 'get_by_{0}'.format(api_resource_key))
    if not args.advisory_format:
        advisories = query_client_func(api_resource_value)
    else:
        if api_resource_key in constants.allows_filter:
            filter = query_client.Filter()
            if args.first_published:
                start_date, end_date = args.first_published
                filter = query_client.FirstPublishedFilter(start_date, end_date)
            elif args.last_published:
                start_date, end_date = args.last_published
                filter = query_client.LastPublishedFilter(start_date, end_date)
            advisories = query_client_func(args.advisory_format, api_resource_value, filter)
        else:
            advisories = query_client_func(args.advisory_format, api_resource_value)

    returned_output = None
    if args.fields:
        if args.count:
            returned_output = [utils.count_fields(advisories, args.fields)]
        else:
            returned_output = utils.filter_advisories(advisories, args.fields)
    else:
        returned_output = utils.filter_advisories(advisories, constants.API_LABELS)

    output_format, file_path = args.output_format

    with utils.get_output_filehandle(file_path) as f:
        utils.output(returned_output, output_format, f)


if __name__ == '__main__':
    main()
