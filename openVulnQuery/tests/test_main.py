import unittest

from openVulnQuery import advisory
from openVulnQuery import config
from openVulnQuery import constants
from openVulnQuery import main

DATE_SEP_TOKEN = ':'
BAD_REQUEST_TOKEN_URL = "https://example.com/as/token.oauth2"
REQUEST_TOKEN_URL = config.REQUEST_TOKEN_URL

NA = constants.NA_INDICATOR
CVRF_TOKEN = constants.CVRF_ADVISORY_FORMAT_TOKEN
OVAL_TOKEN = constants.OVAL_ADVISORY_FORMAT_TOKEN
IOS_TOKEN = constants.IOS_ADVISORY_FORMAT_TOKEN

mock_advisory_title = "Mock Advisory Title"
adv_cfg = {
    'advisory_id': "Cisco-SA-20111107-CVE-2011-0941",
    'sir': "Medium",
    'first_published': "2011-11-07T21:36:55+0000",
    'last_updated': "2011-11-07T21:36:55+0000",
    'cves': ["CVE-2011-0941", NA],
    'cvrf_url': (
        "http://tools.cisco.com/security/center/contentxml/"
        "CiscoSecurityAdvisory/Cisco-SA-20111107-CVE-2011-0941/cvrf/"
        "Cisco-SA-20111107-CVE-2011-0941_cvrf.xml"),
    'bug_ids': "BUGISidf",
    'cvss_base_score': "7.0",
    'advisory_title': "{}".format(mock_advisory_title),
    'publication_url': "https://tools.cisco.com/mockurl",
    'cwe': NA,
    'product_names': ["product_name_1", "product_name_2"],
    'summary': "This is summary"
}
mock_advisory = advisory.CVRF(**adv_cfg)
mock_advisories = [mock_advisory]


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
        self.assertRaises(Exception, main.main, string_list)

    def test_main_advisory_format_from_call_cvrf(self):
        self.assertEqual(
            main.advisory_format_from_call(CVRF_TOKEN), CVRF_TOKEN)

    def test_main_advisory_format_from_call_oval(self):
        self.assertEqual(
            main.advisory_format_from_call(OVAL_TOKEN), OVAL_TOKEN)

    def test_main_advisory_format_from_call_none(self):
        self.assertEqual(
            main.advisory_format_from_call(None), IOS_TOKEN)

    def test_main_advisory_format_from_call_false(self):
        self.assertEqual(
            main.advisory_format_from_call(False), IOS_TOKEN)

    def test_main_advisory_format_from_call_true(self):
        self.assertEqual(
            main.advisory_format_from_call(True), IOS_TOKEN)

    def test_main_advisory_format_from_call_empty(self):
        self.assertEqual(
            main.advisory_format_from_call(''), IOS_TOKEN)

    def test_main_filter_or_aggregate_succeeds(self):
        self.assertTrue(main.filter_or_aggregate(mock_advisories, None, None))

    def test_main_filter_or_aggregate_fields_succeeds(self):
        self.assertTrue(main.filter_or_aggregate(mock_advisories, ['sir'], ''))

    def test_main_filter_or_aggregate_fields_count_succeeds(self):
        self.assertTrue(main.filter_or_aggregate(mock_advisories, ['sir'], 42))

    def test_main_filter_config_succeeds(self):
        self.assertTrue(main.filter_config('no_resource_matches', None, None))

    def test_main_filter_config_all_succeeds(self):
        self.assertTrue(main.filter_config(
            constants.ALLOWS_FILTER[0], '', ''))

    def test_main_filter_config_severity_succeeds(self):
        self.assertTrue(main.filter_config(
            constants.ALLOWS_FILTER[-1], '', ''))

    def test_main_filter_config_all_first_succeeds(self):
        se = '2017-06-20', '2017-06-21'
        self.assertTrue(main.filter_config(
            constants.ALLOWS_FILTER[0], se, ''))

    def test_main_filter_config_all_last_succeeds(self):
        se = '2017-06-20', '2017-06-21'
        self.assertTrue(main.filter_config(
            constants.ALLOWS_FILTER[0], '', se))
