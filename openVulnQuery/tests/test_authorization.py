import unittest

import mock
import requests
from openVulnQuery import authorization
from openVulnQuery import config

CLIENT_ID = 'BadCodedBadCodedBadCoded'
CLIENT_SECRET = 'DeadFaceDeadFaceDeadFace'
REQUEST_TOKEN_URL = config.REQUEST_TOKEN_URL
API_URL = config.API_URL

BAD_REQUEST_TOKEN_URL = "https://example.com/as/token.oauth2"
NOT_FOUND_REQUEST_TOKEN_URL = "https://cloudsso.cisco.com/as/token.oauth2.404"
NOT_FOUND_STATUS = 404
NOT_FOUND_REASON = 'Not Found'
NOT_FOUND_URL_FULL = (
    "{}?client_secret={}&client_id={}"
    "".format(NOT_FOUND_REQUEST_TOKEN_URL, CLIENT_SECRET, CLIENT_ID))
HTTP_ERROR_MSG = '{} Client Error: {} for url: {}'.format(
        NOT_FOUND_STATUS, NOT_FOUND_REASON, NOT_FOUND_URL_FULL)

OK_STATUS = 200
OAUTH2_RESPONSE_BOGUS_BUT_OK = {
    "access_token": "FeedFaceBadCodedDeadBeadFeed",
    "token_type": "Bearer",
    "expires_in": 3599
}


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
                raise requests.exceptions.HTTPError(HTTP_ERROR_MSG)
    url = args[0]
    if url == REQUEST_TOKEN_URL:
        return MockResponse(url, OAUTH2_RESPONSE_BOGUS_BUT_OK, 200)
    return MockResponse(url, None, NOT_FOUND_STATUS).raise_for_status()


class AuthorizationTest(unittest.TestCase):
    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_authorization_smoke_succeeds_mocked(self, mock_post):
        data = authorization.get_oauth_token(
            CLIENT_ID, CLIENT_SECRET, REQUEST_TOKEN_URL)
        self.assertEqual(data, OAUTH2_RESPONSE_BOGUS_BUT_OK['access_token'])

    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_authorization_smoke_raises_mocked(self, mock_post):
        self.assertRaises(
            requests.exceptions.HTTPError,
            authorization.get_oauth_token,
            CLIENT_ID, CLIENT_SECRET, NOT_FOUND_REQUEST_TOKEN_URL)

    @mock.patch('openVulnQuery.authorization.requests.post',
                side_effect=mocked_req_post)
    def test_authorization_smoke_raises_details_mocked(self, mock_post):
        with self.assertRaises(requests.exceptions.HTTPError) as e:
            authorization.get_oauth_token(
                CLIENT_ID, CLIENT_SECRET, NOT_FOUND_REQUEST_TOKEN_URL)
        self.assertEqual(str(e.exception), HTTP_ERROR_MSG)
