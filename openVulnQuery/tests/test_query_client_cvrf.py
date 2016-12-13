import json
import unittest
import mock
from openVulnQuery import query_client
from openVulnQuery import advisory
from openVulnQuery import config

API_URL = "https://api.cisco.com/security/advisories"
test_advisory_id = "Cisco-SA-20111107-CVE-2011-0941"
test_cve = "CVE-2011-0941"
test_severity = "Medium"
test_year = "2011"
response_not_found = '{"error" : "Not Found"}'
response_error = "{'error' : 'Invalid Url'}"

response_generic = """{
    "advisories": [
    {
      "advisoryId": "Cisco-SA-20111107-CVE-2011-0941",
      "sir": "Medium",
      "firstPublished": "2011-11-07T21:36:55+0000",
      "lastUpdated": "2011-11-07T21:36:55+0000",
      "cves": [
        "%s"
      ],
      "cvrfUrl": "http://tools.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/Cisco-SA-20111107-CVE-2011-0941/cvrf/Cisco-SA-20111107-CVE-2011-0941_cvrf.xml",
    "bugIDs": [
        "CSCtj09179"
      ],
      "cvssBaseScore": "7.8",
      "advisoryTitle": "Cisco IOS Software and Cisco Unified Communications Manager Session Initiation Protocol Packet Processing Memory Leak Vulnerability",
      "publicationUrl": "http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/Cisco-SA-20111107-CVE-2011-0941",
      "cwe": [
        "CWE-399"
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
      "summary": "<P>Cisco IOS Software and Cisco Unified Communications Manager contain a vulnerability that could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition.</P>\n<P>The vulnerability is due to improper processing of malformed packets by the affected software.&nbsp; An unauthenticated, remote attacker could exploit this vulnerability by sending malicious network requests to the targeted system.&nbsp; If successful, the attacker could cause the device to become unresponsive, resulting in a DoS condition.</P>\n<P>Cisco confirmed this vulnerability and released software updates.</P>\n<br />\n<br />\n<P>To exploit the vulnerability, an attacker must send malicious SIP packets to affected systems.&nbsp; Most environments restrict external connections using SIP, likely requiring an attacker to have access to internal networks prior to an attack.&nbsp; In addition, in environments that separate voice and data networks, attackers may have no access to networks that service voice traffic and allow the transmission of SIP packets, further increasing the difficulty of an exploit.</P>\n<P>Cisco indicates through the CVSS score that functional exploit code exists; however, the code is not known to be publicly available.</P>"
    }
    ]
    }""" % test_cve

response_advisory_id = """{
    "advisoryId": "%s",
    "sir": "Medium",
    "firstPublished": "2011-11-07T21:36:55+0000",
    "lastUpdated": "2011-11-07T21:36:55+0000",
    "cves": [
    "CVE-2011-0941"
    ],
    "cvrfUrl": "http://tools.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/Cisco-SA-20111107-CVE-2011-0941/cvrf/Cisco-SA-20111107-CVE-2011-0941_cvrf.xml",
    "bugIDs": [
        "CSCtj09179"
      ],
      "cvssBaseScore": "7.8",
      "advisoryTitle": "Cisco IOS Software and Cisco Unified Communications Manager Session Initiation Protocol Packet Processing Memory Leak Vulnerability",
      "publicationUrl": "http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/Cisco-SA-20111107-CVE-2011-0941",
      "cwe": [
        "CWE-399"
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
      "summary": "<P>Cisco IOS Software and Cisco Unified Communications Manager contain a vulnerability that could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition.</P>\n<P>The vulnerability is due to improper processing of malformed packets by the affected software.&nbsp; An unauthenticated, remote attacker could exploit this vulnerability by sending malicious network requests to the targeted system.&nbsp; If successful, the attacker could cause the device to become unresponsive, resulting in a DoS condition.</P>\n<P>Cisco confirmed this vulnerability and released software updates.</P>\n<br />\n<br />\n<P>To exploit the vulnerability, an attacker must send malicious SIP packets to affected systems.&nbsp; Most environments restrict external connections using SIP, likely requiring an attacker to have access to internal networks prior to an attack.&nbsp; In addition, in environments that separate voice and data networks, attackers may have no access to networks that service voice traffic and allow the transmission of SIP packets, further increasing the difficulty of an exploit.</P>\n<P>Cisco indicates through the CVSS score that functional exploit code exists; however, the code is not known to be publicly available.</P>"
    }""" % test_advisory_id


def mocked_get_requests(*args, **kwargs):
    """Mocks requests get method from QueryClient"""

    url = "{base_url}/{path}".format(base_url = API_URL,
                                     path = args[0])
    return mocked_requests_lib_get(url = url).json()


def mocked_requests_lib_get(*args, **kwargs):
    """Mocks library requests.get method"""
    class MockResponse():
        def __init__(self, status_code, json_response):
            self.status_code = status_code
            self.json_response = json_response

        def json(self):
            return json.loads(self.json_response)

        def raise_for_status(self):
            if self.status_code == 404:
                raise Exception("Mock 404 Not Found Exception")
            elif self.status_code == 406:
                raise Exception("Mock 406 HttpError Exception")

    if API_URL in kwargs["url"]:
        if "advisory" in kwargs["url"]:
            return MockResponse(200, response_advisory_id)
        elif any(x in kwargs["url"] for x in ("cve", "severity", "year", "all")):
            return MockResponse(200, response_generic)
        else:
            return MockResponse(404, response_not_found)
    else:
        return MockResponse(406, response_error)


class OpenVulnQueryClientTestCvrf(unittest.TestCase):
    """Unit Test for all function in OpenVulnQueryClient"""
    def setUp(self):
        self.open_vuln_client = query_client.OpenVulnQueryClient(config.CLIENT_ID,
                                                                 config.CLIENT_SECRET)
        self.adv_format = "cvrf"


    @mock.patch("query_client.OpenVulnQueryClient.get_request", side_effect=mocked_get_requests)
    def test_get_by_cve(self, mock_get_requests):
        """Checks if get_by_cve function calls request args with correct arguments"""
        exp_args = "cvrf/cve/%s" % test_cve
        response = self.open_vuln_client.get_by_cve(self.adv_format, test_cve)
        mock_get_requests.assert_called_with(exp_args)

    @mock.patch("query_client.OpenVulnQueryClient.get_request", side_effect=mocked_get_requests)
    def test_get_by_advisory(self, mock_get_requests):
        """Checks if get_by_advisory function calls request args with correct arguments"""
        exp_args = "cvrf/advisory/%s" % test_advisory_id
        response = self.open_vuln_client.get_by_advisory(self.adv_format, test_advisory_id)
        mock_get_requests.assert_called_with(exp_args)

    @mock.patch("query_client.OpenVulnQueryClient.get_request", side_effect=mocked_get_requests)
    def test_get_by_year(self, mock_get_requests):
        """Checks if get_by_year function calls request args with correct arguments"""
        exp_args = "cvrf/year/%s" % test_year
        response = self.open_vuln_client.get_by_year(self.adv_format, year = test_year)
        mock_get_requests.assert_called_with(exp_args)

    @mock.patch("query_client.OpenVulnQueryClient.get_request", side_effect=mocked_get_requests)
    def test_get_by_severity(self, mock_get_requests):
        """Checks if get_by_severity function calls request args with correct arguments"""
        exp_args = "cvrf/severity/%s" % test_severity
        response = self.open_vuln_client.get_by_severity(self.adv_format, severity=test_severity)
        mock_get_requests.assert_called_with(exp_args)

    @mock.patch("query_client.OpenVulnQueryClient.get_request", side_effect=mocked_get_requests)
    def test_get_by_all(self, mock_get_requests):
        """Checks if get_by_all function calls request args with correct arguments"""
        exp_args = "cvrf/all"
        response = self.open_vuln_client.get_by_all(self.adv_format, "all")
        mock_get_requests.assert_called_with(exp_args)

    @mock.patch("requests.get", side_effect=mocked_requests_lib_get)
    def test_get_requests(self, mock_get):
        """Checks if _get_requests function returns correct output"""
        test_path = "cvrf/cve/%s" % test_cve
        response = self.open_vuln_client.get_request(test_path)
        self.assertDictEqual(json.loads(response_generic), response)

    @mock.patch("requests.get", side_effect=mocked_requests_lib_get)
    def test_get_requests_invalid_path(self, mock_get):
        """Checks if get_by_cve function raises exception for bad url path"""
        invalid_test_path = "cvrf/cvoo/%s" % test_cve
        self.assertRaises(Exception, self.open_vuln_client.get_request, invalid_test_path)

    def test_advisory_list(self):
        advisories = json.loads(response_generic)["advisories"]
        advs = self.open_vuln_client.advisory_list(advisories, self.adv_format)
        self.assertIsInstance(advs[0], advisory.CVRF, "This object is not instance of Advisory")


if __name__ == "__main__":
    unittest.main()
