import argparse
import unittest

from openVulnQuery import cli_api

DATE_PARSER_FORMAT = '%Y-%m-%d'
DATE_SEP_TOKEN = ':'


class CliApiTest(unittest.TestCase):
    def test_cli_api_unchanged_date_sep_token(self):
        se = '2017-06-20', '2017-06-21'
        s_e = DATE_SEP_TOKEN.join(se)
        self.assertTupleEqual(
            cli_api.valid_date(s_e), se)

    def test_cli_api_unchanged_date_parser_format(self):
        se = '1999-12-31', '2000-02-28'
        s_e = DATE_SEP_TOKEN.join(se)
        self.assertTupleEqual(
            cli_api.valid_date(s_e), se)

    def test_cli_api_date_date_sep_token_nok(self):
        se = '2017-06-20', '2017-06-21'
        s_e = ' '.join(se)
        with self.assertRaises(argparse.ArgumentTypeError):
            cli_api.valid_date(s_e)

    def test_cli_api_date_parser_format_nok(self):
        se = '19991231', '20000228'
        s_e = DATE_SEP_TOKEN.join(se)
        self.assertRaises(argparse.ArgumentTypeError, cli_api.valid_date, s_e)

    def test_cli_api_date_parser_start_after_end(self):
        se = '2000-02-28', '1999-12-31'
        s_e = DATE_SEP_TOKEN.join(se)
        self.assertRaises(argparse.ArgumentTypeError, cli_api.valid_date, s_e)

    def test_cli_api_date_parser_start_after_now(self):
        se = '9998-12-31', '9999-02-28'
        s_e = DATE_SEP_TOKEN.join(se)
        self.assertRaises(argparse.ArgumentTypeError, cli_api.valid_date, s_e)

    def test_cli_api_date_parser_end_after_now(self):
        se = '1999-12-31', '9999-02-28'
        s_e = DATE_SEP_TOKEN.join(se)
        self.assertRaises(argparse.ArgumentTypeError, cli_api.valid_date, s_e)

    def test_add_options_to_parser_alien_target(self):
        self.assertRaises(
            NotImplementedError, cli_api.add_options_to_parser, '', '')

    def test_parser_factory_dynamic_succeeds(self):
        self.assertTrue(cli_api.parser_factory())

    def test_parser_factory_dynamic_yields_expected_parser_type(self):
        self.assertTrue(
            isinstance(cli_api.parser_factory(), argparse.ArgumentParser))
