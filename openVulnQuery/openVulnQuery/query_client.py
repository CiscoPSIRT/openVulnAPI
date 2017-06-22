import logging

import requests

import advisory
import authorization
import config


class Filter(object):
    def __init__(self):
        self.path = ''
        self.params = None


class LastPublishedFilter(object):
    def __init__(self, start_date, end_date):
        self.path = 'lastpublished'
        self.params = {'startDate': start_date, 'endDate': end_date}


class FirstPublishedFilter(object):
    def __init__(self, start_date, end_date):
        self.path = 'firstpublished'
        self.params = {'startDate': start_date, 'endDate': end_date}


class OpenVulnQueryClient(object):
    """Client sends get request for advisory information from OpenVuln API.

    Attributes:
        auth_token: OAuth2 Token for API authorization.
        headers: Headers containing OAuth2 Token and data type for request.

    """

    def __init__(self, client_id, client_secret, user_agent='TestApp'):
        logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)
        self.auth_token = authorization.get_oauth_token(client_id,
                                                        client_secret)
        self.headers = {"Authorization": "Bearer %s" % self.auth_token,
                        "Accept": "application/json",
                        "User-Agent": user_agent}

    def get_by_all(self, adv_format, all_adv, a_filter):
        """Return all the advisories using requested advisory format"""

        advisories = self.get_request(
            "{adv_format}/{all}/{filter}".format(adv_format=adv_format,
                                                 all=all_adv,
                                                 filter=a_filter.path),
            a_filter.params)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_cve(self, adv_format, cve):
        """Return the advisory using requested cve id"""

        advisories = self.get_request(
            "{adv_format}/cve/{cve}".format(adv_format=adv_format,
                                            cve=cve))
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_advisory(self, adv_format, an_advisory):
        """Return the advisory using requested advisory id"""

        advisories = {'advisories': [self.get_request(
            "{adv_format}/advisory/{advisory}".format(adv_format=adv_format,
                                                      advisory=an_advisory))]}
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_severity(self, adv_format, severity, a_filter=None):
        """Return the advisories using requested severity"""
        if a_filter is None:
            a_filter = Filter()
        advisories = self.get_request(
            "{adv_format}/severity/{severity}/{filter}".format(
                adv_format=adv_format,
                severity=severity,
                filter=a_filter.path),
            params=a_filter.params)
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_year(self, adv_format, year):
        """Return the advisories using requested year"""

        advisories = self.get_request(
            "{adv_format}/year/{year}".format(adv_format=adv_format,
                                              year=year))
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_latest(self, adv_format, latest):
        """Return the advisories using requested latest"""

        advisories = self.get_request(
            "{adv_format}/latest/{latest}".format(adv_format=adv_format,
                                                  latest=latest))
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_product(self, adv_format, product_name):
        """Return advisories by product name"""

        advisories = self.get_request(
            "{adv_format}/product".format(adv_format=adv_format),
            params={'product': product_name})
        return self.advisory_list(advisories['advisories'], adv_format)

    def get_by_ios_xe(self, ios_version):
        """Return advisories by Cisco IOS advisories version"""
        try:
            advisories = self.get_request(
                "iosxe", params={'version': ios_version})
            return self.advisory_list(advisories['advisories'], None)
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(e.response.status_code,
                                                e.response.text)

    def get_by_ios(self, ios_version):
        """Return advisories by Cisco IOS advisories version"""
        try:
            advisories = self.get_request(
                "ios", params={'version': ios_version})
            return self.advisory_list(advisories['advisories'], None)
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(e.response.status_code,
                                                e.response.text)

    def get_request(self, path, params=None):
        """Send get request to OpenVuln API utilizing headers.

        Args:
            path: OpenVuln API path.
            params: url parameters

        Returns:
            JSON of requested arguments for advisory information.

        Raises:
            If requests exhibits anything other than a 200 response.

        """
        self.logger.info("Sending Get Request %s", path)
        r = requests.get(
            url="{base_url}/{path}".format(base_url=config.API_URL, path=path),
            headers=self.headers,
            params=params)
        r.raise_for_status()
        return r.json()

    def advisory_list(self, advisories, adv_format):
        """Converts json into a list of advisory objects.
        :param advisories: A list of dictionaries describing advisories.
        :param adv_format: The target format either in ('cvrf', 'oval') or
            something that evaluates to False (TODO HACK A DID ACK ?) for ios.
        :returns list of advisory instances
        """
        return [advisory.advisory_factory(
                    adv,
                    adv_format if adv_format in ('cvrf', 'opal') else 'ios',
                    self.logger)
                for adv in advisories]
