import unittest
from openVulnQuery import advisory
from openVulnQuery import constants

NA = constants.NA_INDICATOR
IPS_SIG = constants.IPS_SIGNATURE_LABEL
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


class AdvisoryTest(unittest.TestCase):
    def test_advisory_unchanged_na(self):
        self.assertEquals(advisory.NA, NA)

    def test_advisory_ips_sig_map_key_unchanged(self):
        self.assertTrue(IPS_SIG in advisory.IPS_SIG_MAP)

    def test_advisory_filterable_succeeds(self):
        self.assertTrue(advisory.Filterable())
