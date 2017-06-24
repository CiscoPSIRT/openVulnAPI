import unittest
import mock
import pytest
import requests
import json
from openVulnQuery import constants
from openVulnQuery import config
from openVulnQuery import main
from openVulnQuery import advisory

DATE_PARSER_FORMAT = '%Y-%m-%d'
DATE_SEP_TOKEN = ':'
BAD_REQUEST_TOKEN_URL = "https://example.com/as/token.oauth2"
BAD_API_URL = "https://example.com/security/advisories"

NA = constants.NA_INDICATOR
IPS_SIG = constants.IPS_SIGNATURE_LABEL
mock_advisory_title = "Mock Advisory Title"
mock_response = {
    'advisoryId': "Cisco-SA-20111107-CVE-2011-0941",
    'sir': "Medium",
    'firstPublished': "2011-11-07T21:36:55+0000",
    'lastUpdated': "2011-11-07T21:36:55+0000",
    'cves': ["CVE-2011-0941", NA],
    'cvrfUrl': (
        "http://tools.cisco.com/security/center/contentxml/"
        "CiscoSecurityAdvisory/Cisco-SA-20111107-CVE-2011-0941/cvrf/"
        "Cisco-SA-20111107-CVE-2011-0941_cvrf.xml"),
    'bugIDs': "BUGISidf",
    'cvssBaseScore': "7.0",
    'advisoryTitle': "{}".format(mock_advisory_title),
    'publicationUrl': "https://tools.cisco.com/mockurl",
    'cwe': NA,
    'productNames': ["product_name_1", "product_name_2"],
    'summary': "This is summary",
    'ipsSignatures': NA,
}

SAMPLE_CVE = "CVE-2011-0941"
SAMPLE_PRODUCT = "Cisco Unified Communications Manager (CallManager)"
response_sample_cve = """\
{
  "advisories": [
    {
      "cvrfUrl": "https://tools.cisco.com/security/center/contentxml/\
CiscoSecurityAdvisory/Cisco-SA-20111107-$CVE$/cvrf/Cisco-SA-20111107\
-$CVE$_cvrf.xml",
      "bugIDs": [
        "CSCtj09179"
      ],
      "advisoryTitle": "Cisco IOS Software and Cisco Unified Communications\
 Manager Session Initiation Protocol Packet Processing Memory Leak\
 Vulnerability",
      "sir": "Medium",
      "firstPublished": "2011-11-07T16:36:55-0600",
      "lastUpdated": "2011-11-07T16:36:55-0600",
      "publicationUrl": "http://tools.cisco.com/security/center/content/\
CiscoSecurityAdvisory/Cisco-SA-20111107-%(cve)s",
      "cvssBaseScore": "7.8",
      "ipsSignatures": [
        "NA"
      ],
      "productNames": [
        "Cisco Unified Communications Manager (CallManager)",
        "Cisco IOS Software Releases 12.4 T",
        "Cisco IOS Software Release 12.4(2)T",
        "Cisco IOS Software Release 12.4(4)T",
        "Cisco IOS Software Release 12.4(6)T",
        "Cisco IOS Software Release 12.4(9)T",
        "Cisco IOS Software Release 12.4(11)T",
        "Cisco IOS Software Release 12.4(15)T",
        "Cisco IOS Software Release 12.4(20)T",
        "Cisco IOS Software Release 12.4(22)T",
        "Cisco Unified Communications Manager Version 7.1",
        "Cisco IOS Software Release 12.4(24)T",
        "Cisco IOS 15.1M&T",
        "Cisco IOS Software Release 15.1(1)T",
        "Cisco Unified Communications Manager Version 8.0",
        "Cisco IOS Software Release 15.1(2)T",
        "Cisco Unified Communications Manager Version 8.5",
        "Cisco IOS 15.1S",
        "Cisco IOS Software Release 15.1(3)T",
        "Cisco IOS Software Release 15.1(4)M",
        "Cisco IOS Software Release 15.1(1)S",
        "Cisco IOS Software Release 15.1(2)S",
        "Cisco IOS Software Release 15.1(3)S"
      ],
      "advisoryId": "Cisco-SA-20111107-$CVE$",
      "summary": "<P>Cisco IOS Software and Cisco Unified Communications\
 Manager contain a vulnerability that could allow an unauthenticated,\
 remote attacker to cause a denial of service (DoS) condition.</P>
<P>The vulnerability is due to improper processing of malformed packets by\
 the affected software.&nbsp; An unauthenticated, remote attacker could\
 exploit this vulnerability by sending malicious network requests to the\
 targeted system.&nbsp; If successful, the attacker could cause the device\
 to become unresponsive, resulting in a DoS condition.</P>
<P>Cisco confirmed this vulnerability and released software updates.</P>
<br />
<br />
<P>To exploit the vulnerability, an attacker must send malicious SIP packets\
 to affected systems.&nbsp; Most environments restrict external connections\
 using SIP, likely requiring an attacker to have access to internal networks\
 prior to an attack.&nbsp; In addition, in environments that separate voice\
 and data networks, attackers may have no access to networks that service\
 voice traffic and allow the transmission of SIP packets, further increasing\
 the difficulty of an exploit.</P>
 <P>Cisco indicates through the CVSS score\
 that functional exploit code exists; however, the code is not known to be\
 publicly available.</P>",
      "cwe": [
        "CWE-399"
      ],
      "cves": [
        "$CVE$"
      ]
    }
  ]
}
""".replace('\\', '').replace('\n', '')
API_RESPONSE_CVE_OK = json.loads(
    response_sample_cve.replace('$CVE$', SAMPLE_CVE))
CVES_EXPECTED = API_RESPONSE_CVE_OK['advisories'][0]['cves']

CLIENT_ID = 'BadCodedBadCodedBadCoded'
CLIENT_SECRET = 'DeadFaceDeadFaceDeadFace'
REQUEST_TOKEN_URL = config.REQUEST_TOKEN_URL
API_URL = config.API_URL

OK_STATUS = 200

NOT_FOUND_STATUS = 404
NOT_FOUND_REASON = 'Not Found'

NOT_FOUND_TOK_URL = "https://cloudsso.cisco.com/as/token.oauth2.404"
NOT_FOUND_TOK_URL_FULL = (
    "{}?client_secret={}&client_id={}"
    "".format(NOT_FOUND_TOK_URL, CLIENT_SECRET, CLIENT_ID))
TOK_HTTP_ERROR_MSG = '{} Client Error: {} for url: {}'.format(
        NOT_FOUND_STATUS, NOT_FOUND_REASON, NOT_FOUND_TOK_URL_FULL)

OAUTH2_RESPONSE_BOGUS_BUT_OK = {
    "access_token": "FeedFaceBadCodedDeadBeadFeed",
    "token_type": "Bearer",
    "expires_in": 3599
}

NOT_FOUND_API_URL = "https://api.cisco.com/security/advisories.404"
NOT_FOUND_API_URL_FULL = (
    "{}?client_secret={}&client_id={}"
    "".format(NOT_FOUND_API_URL, CLIENT_SECRET, CLIENT_ID))
API_HTTP_ERROR_MSG = '{} Client Error: {} for url: {}'.format(
        NOT_FOUND_STATUS, NOT_FOUND_REASON, NOT_FOUND_API_URL_FULL)

API_RESPONSE_BOGUS_BUT_OK = mock_response


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

def mocked_req_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, url=None, json_in=None, status_code=None):
            self.url = url
            self.json_in = json_in
            self.status_code = status_code

        def json(self):
            return self.json_in

        def raise_for_status(self):
            if self.status_code != OK_STATUS:
                raise requests.exceptions.HTTPError(TOK_HTTP_ERROR_MSG)
    url = args[0]
    if url == REQUEST_TOKEN_URL:
        return MockResponse(url, OAUTH2_RESPONSE_BOGUS_BUT_OK, 200)
    return MockResponse(url, None, NOT_FOUND_STATUS).raise_for_status()


def mocked_req_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, url=None, json_in=None, status_code=None):
            self.url = url
            self.json_in = json_in
            self.status_code = status_code

        def json(self):
            return self.json_in

        def raise_for_status(self):
            if self.status_code != OK_STATUS:
                raise requests.exceptions.HTTPError(API_HTTP_ERROR_MSG)
    url = kwargs['url']
    if url.startswith('{}/cvrf/all'.format(API_URL)):
        return MockResponse(url, API_RESPONSE_CVE_OK, 200)
    elif url.startswith('{}/cvrf/cve'.format(API_URL)):
        return MockResponse(url, API_RESPONSE_CVE_OK, 200)
    elif url.startswith('{}/cvrf/product'.format(API_URL)):
        return MockResponse(url, API_RESPONSE_CVE_OK, 200)
    elif url.startswith('{}/cvrf/severity'.format(API_URL)):
        return MockResponse(url, API_RESPONSE_CVE_OK, 200)
    elif url.startswith('{}/cvrf/year'.format(API_URL)):
        return MockResponse(url, API_RESPONSE_CVE_OK, 200)
    elif url.startswith(API_URL):
        return MockResponse(url, API_RESPONSE_BOGUS_BUT_OK, 200)
    return MockResponse(url, None, NOT_FOUND_STATUS).raise_for_status()



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

    @pytest.mark.skip(
        reason='Marker set, as implementation does not check trivia locally')
    def test_main_ios_xxx_fails(self):
        string_list = '--ios \'15.5(2)T1\' --product ontologicalyoff'.split()
        self.assertTrue(main.main(string_list))
