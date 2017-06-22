import argparse
import constants
import datetime as dt


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

CLI_API_ADVISORY_FORMAT = (
    {
        'action': 'store_const',
        'const': 'cvrf',
        'dest': 'advisory_format',
        'help': (
            'Selects from cvrf advisories, required except for ios and ios_xe'
            ' query'),
        'tokens': ('--cvrf',),
    },
    {
        'action': 'store_const',
        'const': 'oval',
        'dest': 'advisory_format',
        'help': (
            'Selects from oval advisories, required except for ios and ios_xe'
            ' query'),
        'tokens': ('--oval',),
    },
)

CLI_API_API_RESOURCE = (
    {
        'action': 'store_const',
        'const': ('all', 'all'),
        'dest': 'api_resource',
        'help': 'Retrieve all cvrf/oval advisiories',
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
        'help': 'Retrieve latest (number) of advisories',
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
        'type': (lambda x: ('csv', x)),
    },
    {
        'dest': 'output_format',
        'help': 'Output to JSON with file path',
        'metavar': 'filepath',
        'tokens': ('--json',),
        'type': (lambda x: ('json', x)),
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
        'tokens': ('--last_published',),
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
        'help': ('Announced User-Agent hedar value (towards service)'),
        'metavar': 'string',
        'tokens': ('--user-agent',),
    },
)

CLI_API_CONFIG = (
    {
        'dest': 'json_config_path',
        'help': ('Path to JSON file with config'),
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

    if not isinstance(option_parser, (argparse.ArgumentParser,
                                      argparse._MutuallyExclusiveGroup)):
        raise NotImplementedError(
            "Please provide an argparse.ArgumentParser instance, received %s"
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
    p.set_defaults(output_format=('json', None))

    add_options_to_parser(
        p.add_mutually_exclusive_group(required=False),
        CLI_API_ADVISORY_FORMAT)

    add_options_to_parser(
        p.add_mutually_exclusive_group(required=True), CLI_API_API_RESOURCE)

    add_options_to_parser(
        p.add_mutually_exclusive_group(), CLI_API_OUTPUT_FORMAT)

    add_options_to_parser(
        p.add_mutually_exclusive_group(), CLI_API_ADDITIONAL_FILTERS)

    add_options_to_parser(p, CLI_API_PARSER_GENERIC)

    add_options_to_parser(
        p.add_mutually_exclusive_group(required=True), CLI_API_CONFIG)

    return p
