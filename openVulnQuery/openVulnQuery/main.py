import cli_api
import config
import constants
import query_client
import utils


def main(string_list=None):
    args = cli_api.process_command_line(string_list)
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
