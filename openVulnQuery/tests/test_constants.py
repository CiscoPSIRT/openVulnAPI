import unittest

from openVulnQuery import constants

IPS_SIGNATURE_LABEL = 'ips_signatures'

API_LABELS = (
    'advisory_id',
    'advisory_title',
    'bug_ids',
    'cves',
    'cvrf_url',
    'cvss_base_score',
    'cwe',
    'first_fixed',
    'first_published',
    'ios_release',
    IPS_SIGNATURE_LABEL,
    'last_updated',
    'oval_url',
    'product_names',
    'publication_url',
    'sir',
    'summary',
)

IPS_SIGNATURES = (
    'legacy_ips_id',
    'legacy_ips_url',
    'release_version',
    'software_version',
)

ALLOWS_FILTER = (
    'all',
    'severity',
)

NA_INDICATOR = 'NA'

JSON_OUTPUT_FORMAT_TOKEN = 'json'
CSV_OUTPUT_FORMAT_TOKEN = 'csv'

CVRF_ADVISORY_FORMAT_TOKEN = 'cvrf'
OVAL_ADVISORY_FORMAT_TOKEN = 'oval'
IOS_ADVISORY_FORMAT_TOKEN = 'ios'

ADVISORY_FORMAT_TOKENS = (
    CVRF_ADVISORY_FORMAT_TOKEN,
    OVAL_ADVISORY_FORMAT_TOKEN,
    IOS_ADVISORY_FORMAT_TOKEN,
)


class ConstantsTest(unittest.TestCase):
    def test_constants_unchanged_na_indicator(self):
        self.assertEqual(constants.NA_INDICATOR, NA_INDICATOR)

    def test_constants_filters_available(self):
        self.assertEqual(constants.ALLOWS_FILTER, ALLOWS_FILTER)

    def test_constants_unchanged_advisory_tokens(self):
        self.assertEqual(
            constants.ADVISORY_FORMAT_TOKENS, ADVISORY_FORMAT_TOKENS)

    def test_constants_unchanged_json_format_token(self):
        self.assertEqual(
            constants.JSON_OUTPUT_FORMAT_TOKEN, JSON_OUTPUT_FORMAT_TOKEN)

    def test_constants_unchanged_csv_format_token(self):
        self.assertEqual(
            constants.CSV_OUTPUT_FORMAT_TOKEN, CSV_OUTPUT_FORMAT_TOKEN)

    def test_constants_unchanged_cvrf_advisory_format_token(self):
        self.assertEqual(
            constants.CVRF_ADVISORY_FORMAT_TOKEN, CVRF_ADVISORY_FORMAT_TOKEN)

    def test_constants_unchanged_oval_advisory_format_token(self):
        self.assertEqual(
            constants.OVAL_ADVISORY_FORMAT_TOKEN, OVAL_ADVISORY_FORMAT_TOKEN)

    def test_constants_unchanged_ios_advisory_format_token(self):
        self.assertEqual(
            constants.IOS_ADVISORY_FORMAT_TOKEN, IOS_ADVISORY_FORMAT_TOKEN)

    def test_constants_unchanged_ips_signature_label(self):
        self.assertEqual(constants.IPS_SIGNATURE_LABEL, IPS_SIGNATURE_LABEL)

    def test_constants_api_labels_is_non_empty_tuple(self):
        self.assertTrue(isinstance(constants.API_LABELS, tuple))
        self.assertTrue(constants.API_LABELS)

    def test_constants_unique_api_labels(self):
        api_labels = sorted(constants.API_LABELS)
        api_labels_unique = sorted(set(api_labels))
        self.assertEqual(api_labels, api_labels_unique)
