import argparse
import datetime as dt
import json
import os

from . import config
from . import constants


# Validator function required before referencing:
def valid_date(date_text):
    date_parser_format = '%Y-%m-%d'
    try:
        start_date, end_date = date_text.split(':')
        start_date_obj = dt.datetime.strptime(start_date, date_parser_format)
        end_date_obj = dt.datetime.strptime(end_date, date_parser_format)
        if start_date_obj > end_date_obj:
            raise argparse.ArgumentTypeError(
                'StartDate(%s) should me smaller than EndDate(%s)' % (
                    start_date, end_date))
        momentarily = dt.datetime.now()
        if start_date_obj > momentarily or end_date_obj > momentarily:
            raise argparse.ArgumentTypeError('Invalid date %s' % date_text)
        return start_date, end_date
    except ValueError:
        raise argparse.ArgumentTypeError(
            '%s is not a valid date format. Enter date in'
            ' YYYY-MM-DD:YYYY-MM-DD format' % date_text)


# CLI_API_ASPECT = (  # Code is data is code is data is code is ...
#     {
#         'action': 'an_argparse_action',
#         'choices': 'argparse_choices',
#         'const': 'an_argparse_const',
#         'dest': 'an_argparse_dest',
#         'help': ('an_argparse_help'),
#         'metavar': 'an_argparse_metavar',
#         'nargs': 'an_argparse_nargs',
#         'tokens': ('-a', '--abstract'),
#         'type': 'an_argparse_type',
#     },
# )  # Above structures can be fed into argparse parser construction.

'''
CLI_API_ADVISORY_FORMAT = (
    {
        'action': 'store_const',
        'const': constants.CVRF_ADVISORY_FORMAT_TOKEN,
        'dest': 'advisory_format',
        'help': (
            'Selects from cvrf advisories, required except for ios and ios_xe'
            ' query'),
        'tokens': ('--cvrf',),
    },
    {
        'action': 'store_const',
        'const': constants.OVAL_ADVISORY_FORMAT_TOKEN,
        'dest': 'advisory_format',
        'help': (
            'Selects from oval advisories, required except for ios and ios_xe'
            ' query'),
        'tokens': ('--oval',),
    },
)
'''

CLI_API_API_RESOURCE = (
    {
        'action': 'store_const',
        'const': ('all', 'all'),
        'dest': 'api_resource',

        'help': 'Retrieves all advisiories',

      
        'tokens': ('--all',),
    },
    {
        'dest': 'api_resource',
        'help': 'Retrieve advisories by advisory id',
        'metavar': '<advisory-id>',
        'tokens': ('--advisory',),
        'type': (lambda x: ('advisory', x)),
    },
    {
        'dest': 'api_resource',
        'help': 'Retrieve advisories by cve id',
        'metavar': '<CVE-id>',
        'tokens': ('--cve',),
        'type': (lambda x: ('cve', x)),
    },
    {
        'dest': 'api_resource',

        'help': 'Retrieves latest (number) advisories',
        'metavar': 'number',
        'tokens': ('--latest',),
        'type': (lambda x: ('latest', x)),
    },
    {
        'dest': 'api_resource',
        'help': (
            'Retrieve advisories by severity (low, medium, high, critical)'),
        'metavar': '[critical, high, medium, low]',
        'tokens': ('--severity',),
        'type': (lambda x: ('severity', x)),
    },
    {
        'dest': 'api_resource',
        'help': 'Retrieve advisories by year',
        'metavar': 'year',
        'tokens': ('--year',),
        'type': (lambda x: ('year', x)),
    },
    {
        'dest': 'api_resource',
        'help': 'Retrieve advisories by product names',
        'metavar': 'product_name',
        'tokens': ('--product',),
        'type': (lambda x: ('product', x)),
    },
    {
        'dest': 'api_resource',
        'help': (
            'Retrieve advisories affecting user inputted ios_xe version.'
            'Only one version at a time is allowed.'),
        'metavar': 'iosxe_version',
        'tokens': ('--ios_xe',),
        'type': (lambda x: ('ios_xe', x)),
    },
    {
        'dest': 'api_resource',
        'help': (
            'Retrieve advisories affecting user inputted ios version.'
            'Only one version at a time is allowed.'),
        'metavar': 'ios_version',
        'tokens': ('--ios',),
        'type': (lambda x: ('ios', x)),
    },
)

CLI_API_OUTPUT_FORMAT = (
    {
        'dest': 'output_format',
        'help': 'Output to CSV with file path',
        'metavar': 'filepath',
        'tokens': ('--csv',),
        'type': (lambda x: (constants.CSV_OUTPUT_FORMAT_TOKEN, x)),
    },
    {
        'dest': 'output_format',
        'help': 'Output to JSON with file path',
        'metavar': 'filepath',
        'tokens': ('--json',),
        'type': (lambda x: (constants.JSON_OUTPUT_FORMAT_TOKEN, x)),
    },
)

CLI_API_ADDITIONAL_FILTERS = (
    {
        'dest': 'first_published',
        'help': (
            'Filter advisories based on first_published date'
            ' YYYY-MM-DD:YYYY-MM-DD USAGE: followed by severity or all'),
        'metavar': 'YYYY-MM-DD:YYYY-MM-DD',
        'tokens': ('--first_published',),
        'type': valid_date,
    },
    {
        'dest': 'last_published',
        'help': (
            'Filter advisories based on last_published date'
            ' YYYY-MM-DD:YYYY-MM-DD USAGE: followed by severity or all'),
        'metavar': 'YYYY-MM-DD:YYYY-MM-DD',
        'tokens': ('--last_published', '--last_updated'),
        'type': valid_date,
    },
)

CLI_API_PARSER_GENERIC = (
    {
        'action': 'store_true',
        'dest': 'count',  # TODO made destination explicit, verify that OK
        'help': 'Count of any field or fields',
        'tokens': ('-c', '--count'),  # TODO reversed order, verify that OK
    },
    {
        'choices': constants.API_LABELS + constants.IPS_SIGNATURES,
        'dest': 'fields',
        'help': ('Separate fields by spaces to return advisory information.'
                 ' Allowed values are: %s' % ', '.join(constants.API_LABELS)),
        'metavar': '',
        'nargs': '+',
        'tokens': ('-f', '--fields'),  # TODO reversed order, verify that OK
    },
    {
        'dest': 'user_agent',
        'help': 'Announced User-Agent hedar value (towards service)',
        'metavar': 'string',
        'tokens': ('--user-agent',),
    },
)

CLI_API_CONFIG = (
    {
        'dest': 'json_config_path',
        'help': ('Path to JSON file with config (otherwise fallback to'
                 ' environment variables CLIENT_ID and CLIENT_SECRET, or'
                 ' config.py variables, or fail)'),
        'metavar': 'filepath',
        'tokens': ('--config',),
    },
)


def add_options_to_parser(option_parser, options_add_map):
    """Centralized default option provider for parser (dialect optparse).

    :param option_parser: An instance of argparse.ArgumentParser (for now)
        which will be enriched (cf. option_add_map) and returned.
    :param options_add_map: A sequence of dicts with the latter providing per
        option at least:
        - 'tokens' the seq of strings providing the option,
        - 'dest' providing the target  variable/member string name, and
        - 'help' having a string value.
    :return the parser object (Note: Mutates object anyhow => for DRY 'nuff)
    """

    if not isinstance(option_parser, argparse.ArgumentParser):
        if not getattr(option_parser, '__module__', None) == argparse.__name__:
            # Danse to avoid refering argparse._MutuallyExclusiveGroup ...
            raise NotImplementedError(
                "Please provide an argparse.ArgumentParser instance or an"
                " object generated by argparse.ArgumentParser().add_mutually_"
                "exclusive_group(), received %s instead"
                "" % (type(option_parser),))

    for options in options_add_map:
        tokens = options['tokens']
        option_cfg = {k: v for k, v in options.items() if k != 'tokens'}
        option_parser.add_argument(*tokens, **option_cfg)
    return option_parser


def parser_factory():
    """Knit CLI API together and produce an argparse based parser."""
    p = argparse.ArgumentParser(
        prog='openVulnQuery',
        description='Cisco OpenVuln API Command Line Interface')
    p.set_defaults(output_format=(constants.JSON_OUTPUT_FORMAT_TOKEN, None))


    add_options_to_parser(
        p.add_mutually_exclusive_group(required=True), CLI_API_API_RESOURCE)

    add_options_to_parser(
        p.add_mutually_exclusive_group(), CLI_API_OUTPUT_FORMAT)

    add_options_to_parser(
        p.add_mutually_exclusive_group(), CLI_API_ADDITIONAL_FILTERS)

    add_options_to_parser(p, CLI_API_PARSER_GENERIC)

    add_options_to_parser(
        p.add_mutually_exclusive_group(required=False), CLI_API_CONFIG)

    return p


def process_command_line(string_list=None):
    """Interpret parameters given in command line."""

    parser = parser_factory()

    args = parser.parse_args(args=string_list)


    if args.api_resource[0] not in constants.ALLOWS_FILTER:
        if args.first_published or args.last_published:
            parser.error(
                'Only {} based filter can have additional first_published or'
                ' last_published filter'.format(constants.ALLOWS_FILTER))

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
