import requests
import advisory_object
import authorization
import config
import logging
import time
class OpenVulnQueryClient(object):
    """Client sends get request for advisory information from OpenVuln API.

    Attributes:
        auth_token: OAuth2 Token for API authorization.
        headers: Headers containing OAuth2 Token and data type for request.

    """

    def __init__(self, client_id, client_secret):
        logging.basicConfig(level = logging.WARNING)
        self.logger = logging.getLogger(__name__)
        self.auth_token = authorization.get_oauth_token(client_id, client_secret)
        self.headers = {"Authorization" : "Bearer %s" % self.auth_token,
                        "Accept" : "application/json",
                        "User-Agent" : "TestApp"}

    def get_by_all(self, adv_format, all_adv, cvrf_parsed = False):
        """Return all the advisiories using requested advisory format"""

        advisories = self.get_request(
            "{adv_format}/{all}".format(adv_format = adv_format,
                                        all = all_adv))
        return self.advisory_list(advisories['advisories'], cvrf_parsed, adv_format)

    def get_by_cve(self, adv_format, cve, cvrf_parsed = False):
        """Return the advisory using requested cve id"""

        advisories = self.get_request(
            "{adv_format}/cve/{cve}".format(adv_format = adv_format,
                                            cve = cve))
        return self.advisory_list(advisories['advisories'], cvrf_parsed, adv_format)

    def get_by_advisory(self, adv_format, advisory, cvrf_parsed = False):
        """Return the advisory using requested advisory id"""

        advisories = {'advisories': [self.get_request(
            "{adv_format}/advisory/{advisory}".format(adv_format = adv_format,
                                                      advisory = advisory))]}
        return self.advisory_list(advisories['advisories'], cvrf_parsed, adv_format)


    def get_by_severity(self, adv_format, severity, cvrf_parsed = False):
        """Return the advisories using requested severity"""

        advisories = self.get_request(
            "{adv_format}/severity/{severity}".format(adv_format = adv_format,
                                                      severity = severity))
        return self.advisory_list(advisories['advisories'], cvrf_parsed, adv_format)

    def get_by_year(self, adv_format, year, cvrf_parsed = False):
        """Return the advisories using requested year"""

        advisories = self.get_request(
            "{adv_format}/year/{year}".format(adv_format = adv_format,
                                              year = year))
        return self.advisory_list(advisories['advisories'], cvrf_parsed, adv_format)

    def get_by_latest(self, adv_format, latest, cvrf_parsed = False):
        """Return the advisories using requested latest"""

        advisories = self.get_request(
            "{adv_format}/latest/{latest}".format(adv_format = adv_format,
                                                  latest = latest))
        return self.advisory_list(advisories['advisories'], cvrf_parsed, adv_format)

    def get_request(self, path):
        """Send get request to OpenVuln API utilizing headers.

        Args:
            path: OpenVuln API path.

        Returns:
            JSON of requested arguments for advisory information.

        Raises:
            If requests exhibits anything other than a 200 response.

        """
        self.logger.info("Sending Get Request %s", path)
        max_conn_tries = 8
        conn_tries = 0
        while True:
            try:
                r = requests.get(
                    url = "{base_url}/{path}".format(base_url = config.API_URL,
                                                     path = path),
                                                     headers = self.headers,
                                                     timeout = 5)
                break
            except requests.exceptions.Timeout as te:
                self.logger.warning("Timeout Exception")
                conn_tries += 1
                if conn_tries == max_conn_tries:
                    raise Exception("Maximum Connection Tries Exceeded")
        r.raise_for_status()
        self.logger.info("Request sent : Response %s", r.status_code)
        return r.json()

    def advisory_list(self, advisories, cvrf_parsed, adv_format):
        """ Converts json into a list of advisory objects

        Args:
            advisories: A list of dictionaries describing advisories.
            cvrf_parsed: Boolean to determine whether to parse xml for fields.

        Returns:
            List of advisory objects.

        """
        advisory_list = []
        for advisory_dict in advisories:
            adv = advisory_object.Advisory(advisory_dict, cvrf_parsed, adv_format)
            self.logger.debug("Advisory Object %s Created", adv.advisory_id)
            advisory_list.append(adv)
        return advisory_list
