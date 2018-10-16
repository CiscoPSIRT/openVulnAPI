from . import cli_api
from . import config
from . import constants
from . import query_client
from . import utils


def filter_or_aggregate(advisories, fields=None, count=None):
    """Post process depending on requested fields and count aggregation."""
    if fields:
        if count:
            return [utils.count_fields(advisories, fields)]
        else:
            return utils.filter_advisories(advisories, fields)
    else:
        return utils.filter_advisories(advisories, constants.API_LABELS)


def filter_config(resource, first_pub_pair=None, last_pub_pair=None):
    """Provide rule conforming filter config from request of filters and API
    resource(s) requested."""
    if resource in constants.ALLOWS_FILTER:
        # Process eventual filter parameters:
        if first_pub_pair:
            a_filter = query_client.TemporalFilter(
                query_client.PUBLISHED_FIRST, *first_pub_pair)
        elif last_pub_pair:
            a_filter = query_client.TemporalFilter(
                query_client.PUBLISHED_LAST, *last_pub_pair)
        else:  # Default is 'empty' filter
            a_filter = query_client.Filter()
    else:
        a_filter = None

    return {'a_filter': a_filter}


def main(string_list=None):
    args = cli_api.process_command_line(string_list)
    api_resource_key, api_resource_value = args.api_resource

    topic = api_resource_key
    
    if api_resource_key == constants.IOS_ADVISORY_FORMAT_TOKEN:
        adv_format = constants.IOS_ADVISORY_FORMAT_TOKEN
    else:
        adv_format = constants.DEFAULT_ADVISORY_FORMAT_TOKEN

    f_cfg = filter_config(
        api_resource_key, args.first_published, args.last_published)

    client_cfg = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET
    }
    if args.user_agent:
        client_cfg['user_agent'] = args.user_agent
    client = query_client.OpenVulnQueryClient(**client_cfg)

    advisories = client.get_by(topic, adv_format, api_resource_value, **f_cfg)

    output_format, file_path = args.output_format

    with utils.get_output_filehandle(file_path) as f:
        utils.output(filter_or_aggregate(advisories, args.fields, args.count),
                     output_format, f)
