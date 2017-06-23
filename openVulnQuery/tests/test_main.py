import argparse
import unittest
import pytest
import requests.adapters

from openVulnQuery import main
from openVulnQuery import config

DATE_PARSER_FORMAT = '%Y-%m-%d'
DATE_SEP_TOKEN = ':'
BAD_REQUEST_TOKEN_URL = "https://example.com/as/token.oauth2"
BAD_API_URL = "https://example.com/security/advisories"


class MainTest(unittest.TestCase):
    def test_main_smoke_user_error(self):
        with self.assertRaises(SystemExit) as e:
            main.main()
        self.assertEqual(e.exception.code, 2)

    def test_main_smoke_help(self):
        with self.assertRaises(SystemExit) as e:
            main.main(['--help'])
        self.assertEqual(e.exception.code, 0)

    def test_main_smoke_help_short(self):
        with self.assertRaises(SystemExit) as e:
            main.main(['-h'])
        self.assertEqual(e.exception.code, 0)

    def test_main_missing_adv_format(self):
        string_list = '--severity critical'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_unknown_adv_format(self):
        string_list = '--unknown'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_filter_forbidden_by_api(self):
        se = '2017-06-20', '2017-06-21'
        s_e = DATE_SEP_TOKEN.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_filter_date_format_end_missing(self):
        se = '2017-06-20', ''
        s_e = DATE_SEP_TOKEN.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_filter_date_format_sep_bad(self):
        se = '2017-06-20', '2017-06-21'
        s_e = 'P'.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_filter_date_format_end_bad(self):
        se = '2017-06-20', '2017-06-00'
        s_e = DATE_SEP_TOKEN.join(se)
        string_list = (
            '--cvrf --product foo --first_published {}'.format(s_e).split())
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_severity_fails(self):
        string_list = '--ios \'15.5(2)T1\' --severity ontologicalyoff'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_product_fails(self):
        string_list = '--ios \'15.5(2)T1\' --product ontologicalyoff'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_cve_fails(self):
        string_list = '--ios \'15.5(2)T1\' --cve CVE-2017'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_latest_fails(self):
        string_list = '--ios \'15.5(2)T1\' --latest 42'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_advisory_fails(self):
        string_list = '--ios \'15.5(2)T1\' --advisory ontologicalyoff'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_all_fails(self):
        string_list = '--ios \'15.5(2)T1\' --all'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_year_fails(self):
        string_list = '--ios \'15.5(2)T1\' --year 2017'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_ios_unknown_out_format_fails(self):
        string_list = '--ios \'15.5(2)T1\' --yaml so-what.yaml'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_cvrf_version_fails(self):
        string_list = '--cvrf --version 15.5'.split()
        with self.assertRaises(SystemExit) as e:
            main.main(string_list)
        self.assertEqual(e.exception.code, 2)

    def test_main_cvrf_all_fails_wrong_token_url(self):
        string_list = '--cvrf --all'.split()
        config.REQUEST_TOKEN_URL = BAD_REQUEST_TOKEN_URL
        self.assertRaises(requests.adapters.SSLError, main.main, string_list)

    @pytest.mark.skip(
        reason='Marker set, as implementation does not check trivia locally')
    def test_main_ios_xxx_fails(self):
        string_list = '--ios \'15.5(2)T1\' --product ontologicalyoff'.split()
        self.assertTrue(main.main(string_list))
