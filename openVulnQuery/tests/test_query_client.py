import unittest
import mock
import requests
import json
from openVulnQuery import query_client
from openVulnQuery import constants
from openVulnQuery import config
from openVulnQuery import advisory

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


class QueryClientTest(unittest.TestCase):
    def test_query_client_unchanged_adv_tokens(self):
        self.assertEquals(query_client.ADV_TOKENS,
                          constants.ADVISORY_FORMAT_TOKENS)

    def test_query_client_unchanged_temporal_filter_keys(self):
        self.assertTrue(len(query_client.TEMPORAL_FILTER_KEYS) == 2)

    def test_query_client_ensure_adv_format_token_succeeds(self):
        self.assertTrue(query_client.ensure_adv_format_token(''))

    def test_query_client_filter_succeeds(self):
        self.assertTrue(query_client.Filter())

    def test_query_client_temporal_filter_succeeds(self):
        self.assertTrue(query_client.TemporalFilter('', *('',) * 2))

    def test_query_client_first_published_succeeds(self):
        self.assertTrue(query_client.FirstPublished(*('',) * 2))

    def test_query_client_last_updated_succeeds(self):
        self.assertTrue(query_client.LastUpdated(*('',) * 2))

    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_smoke_init_succeeds_mocked(self, mock_post):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        self.assertIsInstance(client, query_client.OpenVulnQueryClient)
        self.assertEqual(
            client.auth_token, OAUTH2_RESPONSE_BOGUS_BUT_OK['access_token'])
        self.assertEqual(
            client.auth_url, REQUEST_TOKEN_URL)

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_smoke_fails_non_topic_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        self.assertRaises(
            KeyError,
            client.get_by,
            'let_this_topic_be_non_existing',
            None,
            None,
            **{})

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_cvrf_succeeds_advisory_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        advisories_as_cvrf = client.get_by(
            'advisory',
            format=constants.CVRF_ADVISORY_FORMAT_TOKEN,
            aspect='non_existing_aspect_on_server',
            **{'a_filter': None})
        self.assertTrue(len(advisories_as_cvrf) == 1)
        cvrf_first = advisories_as_cvrf[0]
        self.assertIsInstance(cvrf_first, advisory.CVRF)
        self.assertEqual(cvrf_first.advisory_id, mock_response['advisoryId'])

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_cvrf_succeeds_cve_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        advisories_as_cvrf = client.get_by(
            'cve',
            format=constants.CVRF_ADVISORY_FORMAT_TOKEN,
            aspect=SAMPLE_CVE,
            **{'a_filter': None})
        self.assertTrue(len(advisories_as_cvrf) == 1)
        cvrf_first = advisories_as_cvrf[0]
        self.assertIsInstance(cvrf_first, advisory.CVRF)
        self.assertEqual(cvrf_first.cves, CVES_EXPECTED)

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_cvrf_succeeds_product_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        advisories_as_cvrf = client.get_by(
            'product',
            format=constants.CVRF_ADVISORY_FORMAT_TOKEN,
            aspect=SAMPLE_PRODUCT,
            **{'a_filter': None})
        self.assertTrue(len(advisories_as_cvrf) == 1)
        cvrf_first = advisories_as_cvrf[0]
        self.assertIsInstance(cvrf_first, advisory.CVRF)
        self.assertIn(SAMPLE_PRODUCT, cvrf_first.product_names)

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_cvrf_succeeds_year_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        sample_year = 2017
        advisories_as_cvrf = client.get_by(
            'year',
            format=constants.CVRF_ADVISORY_FORMAT_TOKEN,
            aspect=sample_year,
            **{'a_filter': None})
        self.assertTrue(len(advisories_as_cvrf) == 1)
        cvrf_first = advisories_as_cvrf[0]
        self.assertIsInstance(cvrf_first, advisory.CVRF)

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_cvrf_succeeds_severity_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        sample_severity = 'high'
        advisories_as_cvrf = client.get_by(
            'severity',
            format=constants.CVRF_ADVISORY_FORMAT_TOKEN,
            aspect=sample_severity,
            a_filter=query_client.Filter()
        )
        self.assertTrue(len(advisories_as_cvrf) == 1)
        cvrf_first = advisories_as_cvrf[0]
        self.assertIsInstance(cvrf_first, advisory.CVRF)

    @mock.patch('openVulnQuery.query_client.requests.get',
                side_effect=mocked_req_get)
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_cvrf_all_succeeds_mocked(self, mock_post, mock_get):
        client = query_client.OpenVulnQueryClient(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL, user_agent='foo')
        sample_all = 'all'
        advisories_as_cvrf = client.get_by(
            'all',
            format=constants.CVRF_ADVISORY_FORMAT_TOKEN,
            aspect=sample_all,
            a_filter=query_client.Filter()
        )
        self.assertTrue(len(advisories_as_cvrf) == 1)
        cvrf_first = advisories_as_cvrf[0]
        self.assertIsInstance(cvrf_first, advisory.CVRF)

    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_client_smoke_not_found_tok_url_raises_mocked(self, mock_post):
        self.assertRaises(
            requests.exceptions.HTTPError,
            query_client.OpenVulnQueryClient,
            CLIENT_ID, CLIENT_SECRET, NOT_FOUND_TOK_URL, user_agent='foo')

    # @mock.patch('openVulnQuery.authorization.requests.post',
    #             side_effect=mocked_req_post)
    # def test_authorization_smoke_raises_details_mocked(self, mock_post):
    #     with self.assertRaises(requests.exceptions.HTTPError) as e:
    #         query_client.get_oauth_token(
    #             CLIENT_ID, CLIENT_SECRET, NOT_FOUND_TOK_URL)
    #     self.assertEqual(str(e.exception), TOK_HTTP_ERROR_MSG)
