import datetime as dt
import json
import logging
import os
import uuid

import requests

from . import advisory
from . import authorization
from . import config
from . import constants
from . import rest_api

ADV_TOKENS = constants.ADVISORY_FORMAT_TOKENS

TEMPORAL_FILTER_KEYS = ('startDate', 'endDate')
PUBLISHED_FIRST = 'firstpublished'
PUBLISHED_LAST = 'lastpublished'
TEMPORAL_PUBLICATION_ASPECTS = (PUBLISHED_FIRST, PUBLISHED_LAST)

DEBUG_API_USAGE = os.getenv('CISCO_OPEN_VULN_API_DEBUG', None)
DEBUG_API_PATH = os.getenv('CISCO_OPEN_VULN_API_PATH', None)
DEBUG_TIME_STAMP_FORMAT = "%Y%m%dT%H%M%S.%f"

def ensure_adv_format_token(adv_format):
    return adv_format if adv_format in ADV_TOKENS else ADV_TOKENS[-1]

class Filter(object):
    def __init__(self, path='', params=None):
        self.path = path
        self.params = params


class TemporalFilter(object):
    def __init__(self, path, *args):
        self.path = path  # Better be in TEMPORAL_PUBLICATION_ASPECTS ...
        self.params = dict(zip(TEMPORAL_FILTER_KEYS, args))


class FirstPublished(TemporalFilter):
    def __init__(self, *args):
        super(FirstPublished, self).__init__(PUBLISHED_FIRST, *args)


class LastUpdated(TemporalFilter):
    def __init__(self, *args):
        super(LastUpdated, self).__init__(PUBLISHED_LAST, *args)


class OpenVulnQueryClient(object):
    """Client sends get request for advisory information from OpenVuln API.

    :var auth_token: OAuth2 Token for API authorization.
    :var headers: Headers containing OAuth2 Token and data type for
     request.
    """

    def __init__(self, client_id, client_secret, auth_url=None,
                 user_agent='TestApp'):
        """
        :param client_id: Client application Id as retrieved from API provider
        :param client_secret: Client secret as retrieved from API provider
        :param auth_url: POST URL to request auth token response (default
            from config)
        :param user_agent: Communicates the name of the app per request.

        """
        logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)
        self.auth_url = auth_url if auth_url else config.REQUEST_TOKEN_URL
        self.auth_token = authorization.get_oauth_token(
            client_id, client_secret, request_token_url=self.auth_url)
        self.headers = rest_api.rest_with_auth_headers(
            self.auth_token, user_agent)

    def get_by_all(self, adv_format, all_adv, a_filter):
        """Return all the advisories using requested advisory format"""
        req_cfg = {
            'filter': a_filter.path,
        }
        req_path = "all/{filter}".format(**req_cfg)
        advisories = self.get_request(req_path, a_filter.params)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_cve(self, adv_format, cve_id, a_filter=None):
        """Return the advisory using requested cve id"""
        req_cfg = {
            'cve_id': cve_id,
        }
        req_path = "cve/{cve_id}".format(**req_cfg)
        advisories = self.get_request(req_path)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_advisory(self, adv_format, an_advisory, a_filter=None):
        """Return the advisory using requested advisory id"""
        req_cfg = {
            'advisory': an_advisory,
        }
        req_path = "advisory/{advisory}".format(**req_cfg)
        advisories = self.get_request(req_path)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_severity(self, adv_format, severity, a_filter=None):
        """Return the advisories using requested severity"""
        req_cfg = {
            'severity': severity,
            'filter': Filter().path if a_filter is None else a_filter.path,
        }
        req_path = ("severity/{severity}/{filter}"
                    "".format(**req_cfg))
        advisories = self.get_request(req_path, params=a_filter.params)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_year(self, adv_format, year, a_filter=None):
        """Return the advisories using requested year"""
        req_cfg = {
            'year': year,
        }
        req_path = "year/{year}".format(**req_cfg)
        advisories = self.get_request(req_path)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_latest(self, adv_format, latest, a_filter=None):
        """Return the advisories using requested latest"""
        req_cfg = {
            'latest': latest,
        }
        req_path = "latest/{latest}".format(**req_cfg)
        advisories = self.get_request(req_path)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_product(self, adv_format, product_name, a_filter=None):
        """Return advisories by product name"""

        '''
        TODO: It was discovered that the endpoint url in the documentation
        is incorrect. get_by_product should work AFTER the endpoint url path
        is properly edited to match the documentation; that is, to /security/advisories/product
        instead of the old /cvrf /oval urls. This will be done in December 2018. 
        '''
        req_path = "product"
        advisories = self.get_request(
            req_path, params={'product': product_name})
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_ios_xe(self, adv_format, ios_version, a_filter=None):
        """Return advisories by Cisco IOS advisories version"""
        req_path = "iosxe"
        try:
            advisories = self.get_request(
                req_path,
                params={'version': ios_version})
            return self.advisory_list(advisories['advisories'], None)
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(
                e.response.status_code, e.response.text)

    def get_by_ios(self, adv_format, ios_version, a_filter=None):
        """Return advisories by Cisco IOS advisories version"""
        req_path = "ios"
        try:
            advisories = self.get_request(
                req_path,
                params={'version': ios_version})
            return self.advisory_list(advisories['advisories'], None)
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(
                e.response.status_code, e.response.text)

    def get_by(self, topic, format, aspect, **kwargs):
        """Cartesian product ternary paths biased REST dispatcher."""
        trampoline = {  # key: function; required and [optional] parameters
            'all': self.get_by_all,  # format, all_adv, a_filter
            'cve': self.get_by_cve,  # format, cve, [a_filter]
            'advisory': self.get_by_advisory,  # format, an_advisory,[a_filter]
            'severity': self.get_by_severity,  # format, severity, [a_filter]
            'year': self.get_by_year,  # format, year, [a_filter]
            'latest': self.get_by_latest,  # format, latest, [a_filter]
            'product': self.get_by_product,  # format, product_name, [a_filter]
            'ios_xe': self.get_by_ios_xe,  # 'ios', ios_version, [a_filter]
            'ios': self.get_by_ios,  # 'ios', ios_version, [a_filter]
        }
        if topic not in trampoline:
            raise KeyError(
                "REST API 'topic' ({}) not (yet) supported.".format(topic))

        return trampoline[topic](format, aspect, **kwargs)

    def get_request(self, path, params=None):
        """Send get request to OpenVuln API utilizing headers.

        :param path: OpenVuln API path.
        :param params: url parameters
        :return JSON of requested arguments for advisory information.
        :raise HTTPError for anything other than a 200 response.
        """
        self.logger.info("Sending Get Request %s", path)
        req_cfg = {'base_url': config.API_URL, 'path': path}
        req_url = "{base_url}/{path}".format(**req_cfg)
        request_data = {
            'url': req_url,
            'headers': self.headers,
            'params': params,
        }
        request_id = request_snapshot(request_data)
        r = requests.get(**request_data)
        r.raise_for_status()
        if request_id:
            response_snapshots(r.json(), request_id)
        return r.json()

    def advisory_list(self, advisories, adv_format):
        """Converts json into a list of advisory objects.

        :param advisories: A list of dictionaries describing advisories.
        :param adv_format: The target format in default format or
            something that evaluates to False (TODO HACK A DID ACK ?) for ios.
        :return list of advisory instances
        """
        adv_format = ensure_adv_format_token(adv_format)
        return [advisory.advisory_factory(adv, adv_format, self.logger)
                for adv in advisories]


def snapshot_timestamp():
    """Generate timestamp in format DEBUG_TIME_STAMP_FORMAT."""
    return dt.datetime.now().strftime(DEBUG_TIME_STAMP_FORMAT)


def snapshot_name(kind, correlating_id, time_stamp=None):
    """Generate a snapshot name for kind and correlating id (by request).
    :var kind: A string that will be lower cased and postfixed (before
        extension) to the filename.
    :var correlating_id: A string id to correlate multiple snapshots.
    :var time_stamp: A string rep of a time stamp or None
    :return A filename.
    """
    if time_stamp is None:
        time_stamp = snapshot_timestamp()
    return ('ts-{}_id-{}_snapshot-of-{}.json'
            ''.format(time_stamp, correlating_id, kind.lower()))


def request_snapshot(data):
    """If env has CISCO_OPEN_VULN_API_DEBUG set (and evaluates to True)
    dump the data from the request to an existing folder as set by either env
    variable CISCO_OPEN_VULN_API_PATH or default taking the current folder.

    :var data: Request data as dict.
    :return unique request id, to ease matching to response snapshots or None
        if no debugging requested.
    """
    if not DEBUG_API_USAGE:
        return None
    request_id = str(uuid.uuid4())
    file_path = snapshot_name('request', request_id)
    if DEBUG_API_PATH:
        file_path = os.path.join(DEBUG_API_PATH, file_path)
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, encoding='utf-8')
    except (OSError, ValueError):
        pass  # Best effort snapshots ;-)

    return request_id


def response_snapshots(data, request_id):
    """If env has CISCO_OPEN_VULN_API_DEBUG set (and evaluates to True)
    dump the data from the response to an existing folder as set by either env
    variable CISCO_OPEN_VULN_API_PATH or default taking the current folder.

    :var data: Repsonse data as received from requests json method (no json!).
    :var unique request id, to ease matching to request snapshot.
    """
    if not DEBUG_API_USAGE:
        return None

    time_stamp = snapshot_timestamp()
    file_path = snapshot_name('response-raw', request_id, time_stamp)
    if DEBUG_API_PATH:
        file_path = os.path.join(DEBUG_API_PATH, file_path)
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, encoding='utf-8')
    except (OSError, ValueError):
        pass  # Best effort snapshots ;-)

    file_path = snapshot_name('response-formatted', request_id, time_stamp)
    if DEBUG_API_PATH:
        file_path = os.path.join(DEBUG_API_PATH, file_path)
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4, encoding='utf-8')
    except (OSError, ValueError):
        pass  # ditto (cf. above)
