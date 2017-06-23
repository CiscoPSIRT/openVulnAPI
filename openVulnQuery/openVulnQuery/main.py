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
        # Try next environment variables are set, then config.py, or fail:
        keys_required = ('CLIENT_ID', 'CLIENT_SECRET')
        env_config = {k: os.getenv(k, None) for k in keys_required}

        if all([v for v in env_config.values()]):  # OK, take env values:
            for key in keys_required:
                setattr(config, key, env_config[key])
        elif all([getattr(config, k, None) for k in keys_required]):
            pass  # Fallback to the credentials in config.py (non-empty!)
        else:
            parser.error(
                ' --conf <FILE> ? Missing configuration file (credentials)')
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

    topic = api_resource_key

    if args.advisory_format:
        adv_format = args.advisory_format
    else:
        adv_format = constants.ADVISORY_FORMAT_TOKENS[-1]

    f_cfg = {'a_filter': None}
    if api_resource_key in constants.ALLOWS_FILTER:
        # Process eventual filter parameters:
        if args.first_published:
            f_cfg['a_filter'] = query_client.TemporalFilter(
                query_client.PUBLISHED_FIRST, *args.first_published)
        elif args.last_published:
            f_cfg['a_filter'] = query_client.TemporalFilter(
                query_client.PUBLISHED_LAST, *args.last_published)
        else:  # Default is 'empty' filter
            f_cfg['a_filter'] = query_client.Filter()

    client_cfg = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET
    }
    if args.user_agent:
        client_cfg['user_agent'] = args.user_agent
    client = query_client.OpenVulnQueryClient(**client_cfg)

    advisories = client.get_by(topic, adv_format, api_resource_value, **f_cfg)
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
