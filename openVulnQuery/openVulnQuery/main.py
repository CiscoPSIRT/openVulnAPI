import json
import os

import cli_api
import config
import constants
import query_client
import utils


def process_command_line():
    """Interpret parameters given in command line."""

    parser = cli_api.parser_factory()

    args = parser.parse_args()
    if not args.advisory_format:
        key, val = args.api_resource
        if key not in ['ios', 'ios_xe']:
            parser.error('Advisory format --cvrf or --oval required except for'
                         ' ios and ios_xe')

    if args.api_resource[0] not in constants.ALLOWS_FILTER:
        if args.first_published or args.last_published:
            parser.error(
                'Only %s based filter can have additional first_published or'
                ' last_published filter' % constants.ALLOWS_FILTER)

    if not args.json_config_path:
        parser.error(
            ' --conf <FILE> ? Missing configuration file (with credentials)')
    else:
        if not os.path.isfile(args.json_config_path):
            parser.error(
                'Configuration file not found at %s' % args.json_config_path)
        else:
            parsed_config = json.load(open(args.json_config_path))
            keys_required = ('CLIENT_ID', 'CLIENT_SECRET')
            for key in keys_required:
                setattr(config, key, parsed_config[key])
            keys_optional = ('REQUEST_TOKEN_URL', 'API_URL')
            for key in keys_optional:
                if key in parsed_config:
                    setattr(config, key, parsed_config[key])

    return args


def main():
    args = process_command_line()
    api_resource_key, api_resource_value = args.api_resource

    client_cfg = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET
    }
    if args.user_agent:
        client_cfg['user_agent'] = args.user_agent
    client = query_client.OpenVulnQueryClient(**client_cfg)
    query_client_func = getattr(client, 'get_by_{0}'.format(api_resource_key))
    if not args.advisory_format:
        advisories = query_client_func(api_resource_value)
    else:
        if api_resource_key in constants.ALLOWS_FILTER:
            a_filter = query_client.Filter()
            if args.first_published:
                start_date, end_date = args.first_published
                a_filter = query_client.FirstPublishedFilter(
                    start_date, end_date)
            elif args.last_published:
                start_date, end_date = args.last_published
                a_filter = query_client.LastPublishedFilter(
                    start_date, end_date)
            advisories = query_client_func(
                args.advisory_format, api_resource_value, a_filter)
        else:
            advisories = query_client_func(
                args.advisory_format, api_resource_value)

    if args.fields:
        if args.count:
            returned_output = [utils.count_fields(advisories, args.fields)]
        else:
            returned_output = utils.filter_advisories(advisories, args.fields)
    else:
        returned_output = utils.filter_advisories(
            advisories, constants.API_LABELS)

    output_format, file_path = args.output_format

    with utils.get_output_filehandle(file_path) as f:
        utils.output(returned_output, output_format, f)


if __name__ == '__main__':
    main()
