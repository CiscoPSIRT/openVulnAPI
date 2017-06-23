import unittest
from openVulnQuery import query_client
from openVulnQuery import constants


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
