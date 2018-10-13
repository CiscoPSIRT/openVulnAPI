import argparse
import unittest
import os
import inspect

from openVulnQuery import config
from openVulnQuery import cli_api

DATE_PARSER_FORMAT = '%Y-%m-%d'
DATE_SEP_TOKEN = ':'
SAMPLE_CLIENT_ID = 'BadCodedBadCodedBadCoded'
SAMPLE_CLIENT_SECRET = 'DeadFaceDeadFaceDeadFace'

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

    def test_cli_api_process_command_line_help(self):
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(['--help'])
        self.assertEqual(e.exception.code, 0)

    def test_cli_api_process_command_line_help_short(self):
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(['-h'])
        self.assertEqual(e.exception.code, 0)

    def test_cli_api_process_command_line_missing_adv_format(self):
        string_list = '--severity critical'.split()
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_cli_api_process_command_line_filter_forbidden_by_api(self):
        se = '2017-06-20', '2017-06-21'
        s_e = DATE_SEP_TOKEN.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_cli_api_process_command_line_filter_date_format_end_missing(self):
        se = '2017-06-20', ''
        s_e = DATE_SEP_TOKEN.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_cli_api_process_command_line_filter_date_format_sep_bad(self):
        se = '2017-06-20', '2017-06-21'
        s_e = 'P'.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_cli_api_process_command_line_filter_date_format_end_bad(self):
        se = '2017-06-20', '2017-06-00'
        s_e = DATE_SEP_TOKEN.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(string_list)
        self.assertEqual(e.exception.code, 2)

    # CVRF format as precondition value
    def test_cli_api_process_command_line_cvrf_all_succeeds(self):
        string_list = '--cvrf --all'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_severity_succeeds(self):
        string_list = '--cvrf --severity critical'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_year_succeeds(self):
        string_list = '--cvrf --year 2017'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_product_succeeds(self):
        string_list = '--cvrf --product foo'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_all_json_stdout_succeeds(self):
        string_list = '--cvrf --all --json \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_all_json_file_succeeds(self):
        string_list = '--cvrf --all --json foo.json'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_all_csv_stdout_succeeds(self):
        string_list = '--cvrf --all --csv \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_cvrf_all_csv_file_succeeds(self):
        string_list = '--cvrf --all --csv foo.csv'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    # OVAL format as precondition value
    def test_cli_api_process_command_line_oval_all_succeeds(self):
        string_list = '--oval --all'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_severity_succeeds(self):
        string_list = '--oval --severity critical'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_year_succeeds(self):
        string_list = '--oval --year 2017'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_product_succeeds(self):
        string_list = '--oval --product foo'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_all_json_stdout_succeeds(self):
        string_list = '--oval --all --json \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_all_json_file_succeeds(self):
        string_list = '--oval --all --json foo.json'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_all_csv_stdout_succeeds(self):
        string_list = '--oval --all --csv \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_oval_all_csv_file_succeeds(self):
        string_list = '--oval --all --csv foo.csv'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    # IOS format as precondition value
    # ios ...
    def test_cli_api_process_command_line_ios_all_succeeds(self):
        string_list = '--ios \'15.5(2)T1\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_all_json_stdout_succeeds(self):
        string_list = '--ios \'15.5(2)T1\' --json \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_all_json_file_succeeds(self):
        string_list = '--ios \'15.5(2)T1\' --json foo.json'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_all_csv_stdout_succeeds(self):
        string_list = '--ios \'15.5(2)T1\' --csv \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_all_csv_file_succeeds(self):
        string_list = '--ios \'15.5(2)T1\' --csv foo.csv'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    # ios_xe ...
    def test_cli_api_process_command_line_ios_xe_all_succeeds(self):
        string_list = '--ios_xe \'3.16.1aS\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_xe_all_json_stdout_succeeds(self):
        string_list = '--ios_xe \'3.16.1aS\' --json \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_xe_all_json_file_succeeds(self):
        string_list = '--ios_xe \'3.16.1aS\' --json foo.json'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_xe_all_csv_stdout_succeeds(self):
        string_list = '--ios_xe \'3.16.1aS\' --csv \'\''.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    def test_cli_api_process_command_line_ios_xe_all_csv_file_succeeds(self):
        string_list = '--ios_xe \'3.16.1aS\' --csv foo.csv'.split()
        self.assertTrue(cli_api.process_command_line(string_list))

    # Config aspects
    def test_cli_api_process_command_line_cvrf_all_config_file_not_exist(self):
        string_list = '--cvrf --all --config NOT_PRESENT_PLEASE'.split()
        with self.assertRaises(SystemExit) as e:
            cli_api.process_command_line(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_cli_api_process_command_line_cvrf_all_config_sample_file(self):
        cfg_name = 'sample_credentials.json'
        cfg_dir = os.path.dirname(os.path.abspath(
            inspect.getsourcefile(cli_api)))
        cfg_path = os.path.join(cfg_dir, cfg_name)
        string_list = '--cvrf --all --config {}'.format(cfg_path).split()
        args = cli_api.process_command_line(string_list)
        self.assertEqual(config.CLIENT_ID, SAMPLE_CLIENT_ID)
        self.assertEqual(config.CLIENT_SECRET, SAMPLE_CLIENT_SECRET)

    def test_cli_api_process_command_line_cvrf_all_config_wrong_file(self):
        cfg_name = '__init__.py'
        cfg_dir = os.path.dirname(os.path.abspath(
            inspect.getsourcefile(cli_api)))
        cfg_path = os.path.join(cfg_dir, cfg_name)
        string_list = '--cvrf --all --config {}'.format(cfg_path).split()
        self.assertRaises(
            ValueError, cli_api.process_command_line, string_list)
