import unittest
from openVulnQuery import constants
from openVulnQuery import utils
from openVulnQuery import advisory

NA = constants.NA_INDICATOR
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


class UtilsTest(unittest.TestCase):

    def test_filter_advisories_general_input(self):
        fields = ["advisory_title", "sir", "bug_ids"]
        expected_output = [
            {"advisory_title": "Mock Advisory Title",
             "sir": "Medium",
             "bug_ids": "BUGISidf"}]
        output = utils.filter_advisories(mock_advisories, fields)
        self.assertListEqual(output, expected_output)

    def test_filter_advisories_empty_fields(self):
        fields = []
        expected_output = [{}]
        self.assertListEqual(
            utils.filter_advisories(mock_advisories, fields), expected_output)

    def test_filter_advisories_invalid_fields(self):
        fields = ["advisory_title", "v_score"]
        expected_output = [{'advisory_title': '%s' % mock_advisory_title}]
        output = utils.filter_advisories(mock_advisories, fields)
        self.assertIsInstance(output, list)
        self.assertDictEqual(output[0], expected_output[0])

    def test_count_fields_valid_input(self):
        fields = ["bug_ids", "advisory_title"]
        expected_output = {'bug_ids': 1, 'advisory_title': 1}
        output = utils.count_fields(mock_advisories, fields)
        self.assertDictEqual(output, expected_output)

    def test_count_fields_invalid_input(self):
        fields = ["bug_ids", "v_score"]
        expected_output = {'bug_ids': 1, 'v_score': 0}
        output = utils.count_fields(mock_advisories, fields)
        self.assertDictEqual(output, expected_output)

    def test_get_count_valid(self):
        self.assertEqual(utils.get_count(
            getattr(mock_advisory, "advisory_title")), 1)
        self.assertEqual(utils.get_count(
            getattr(mock_advisory, "product_names")), 2)

    def test_get_count_fields_with_NA(self):
        self.assertEqual(utils.get_count(getattr(mock_advisory, "cwe")), 0)
        self.assertEqual(utils.get_count(getattr(mock_advisory, "cves")), 1)

    def test_flatten_list_void_pair(self):
        naive_void = [{}, {}]
        self.assertListEqual(utils.flatten_list(naive_void), naive_void)

    def test_flatten_list_distinct_pair(self):
        naive_distinct = [{'foo': 'bar'}, {'baz': ''}]
        naive_distinct_side_effected = [{'foo': 'bar'}, {'baz': None}]
        self.assertListEqual(
            utils.flatten_list(naive_distinct), naive_distinct_side_effected)

    # def test_flatten_list_distinct_nested_pair(self):
    #     naive_distinct = [{'foo': 'bar'}, {'baz': {'yes': 'no'}}]
    #     naive_distinct_side_effected = [{'foo': 'bar'}, {'baz': None}]
    #     self.assertListEqual(
    #         utils.flatten_list(naive_distinct), naive_distinct_side_effected)
    #
    # def test_private_reduce_list_dict(self):
    #     k = 'no'
    #     v = [{'no': {'foo': 'bar', 'baz': 'yes'}},
    #          {'no': {'foo': 'bar', 'baz': 'yes'}},
    #          {'yes': {'foo': 'bar', 'baz': 'maybe'}}]
    #     whatever = []
    #     self.assertListEqual(
    #         utils._reduce_list_dict(k, v), whatever)

    def test_private_get_headers_distinct(self):
        naive_distinct = [{'foo': 'bar'}, {'baz': ''}]
        expected = ['baz', 'foo']
        self.assertListEqual(
            sorted(utils._get_headers(naive_distinct)), expected)
