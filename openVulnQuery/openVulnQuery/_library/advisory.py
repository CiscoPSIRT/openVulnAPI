from abc import ABCMeta

from . import constants
from ._compatibility import is_unicode_or_bytes

NA = constants.NA_INDICATOR
IPS_SIG = constants.IPS_SIGNATURE_LABEL

ADVISORIES_COMMONS_MAP = {
    'advisory_id': "advisoryId",
    'advisory_title': "advisoryTitle",
    'bug_ids': "bugIDs",
    'cves': "cves",
    'cvss_base_score': "cvssBaseScore",
    'cwe': "cwe",
    'first_published': "firstPublished",
    'last_updated': "lastUpdated",
    'product_names': "productNames",
    'publication_url': "publicationUrl",
    'sir': "sir",
    'summary': "summary",
}

IPS_SIG_MAP = {
    IPS_SIG: 'ipsSignatures',
}

IOS_ADD_ONS_MAP = {
    'first_fixed': 'firstFixed',
    'ios_release': 'iosRelease',
}


class Filterable(object):
    """Filterable mixin class"""

    def filter(self, *args):
        filtered_dict = {}
        for arg in args:
            if hasattr(self, arg):
                attr = getattr(self, arg)
                if (isinstance(attr, list) and
                        attr and
                        isinstance(attr[0], Filterable)):
                    filtered_dict[arg] = [a.filter(*args) for a in attr]
                else:
                    filtered_dict[arg] = attr
        return filtered_dict


class Advisory(Filterable):
    """Abstract Advisory object"""

    __metaclass__ = ABCMeta

    def __init__(self, advisory_id, sir, first_published, last_updated, cves,
                 bug_ids, cvss_base_score, advisory_title, publication_url,
                 cwe,
                 product_names, summary):
        self.advisory_id = advisory_id
        self.sir = sir
        self.first_published = first_published
        self.last_updated = last_updated
        self.cves = cves
        self.bug_ids = bug_ids
        self.cvss_base_score = cvss_base_score
        self.advisory_title = advisory_title
        self.publication_url = publication_url
        self.cwe = cwe
        self.product_names = product_names
        self.summary = summary


class AdvisoryDefault(Advisory):
    """Default object inherits from Advisory"""

    def __init__(self, *args, **kwargs):
        self.ips_signatures = []
        if IPS_SIG in kwargs:
            self.ips_signatures = [
                IPSSignature(**kw) if not is_unicode_or_bytes(kw) else NA
                for kw in kwargs.pop(IPS_SIG)]
        super(AdvisoryDefault, self).__init__(*args, **kwargs)

class AdvisoryIOS(Advisory):
    """Advisory Object with additional information on IOS/IOSXE version """

    def __init__(self, *args, **kwargs):
        self.first_fixed = kwargs.pop('first_fixed', None)
        self.ios_release = kwargs.pop('ios_release', None)
        super(AdvisoryIOS, self).__init__(*args, **kwargs)


class IPSSignature(Filterable):
    def __init__(self, legacyIpsId, releaseVersion, softwareVersion,
                 legacyIpsUrl):
        self.legacy_ips_id = legacyIpsId
        self.release_version = releaseVersion
        self.software_version = softwareVersion
        self.legacy_ips_url = legacyIpsUrl


def advisory_format_factory_map():
    """Map the advisory format tokens to callable instantiators."""
    return dict(zip(
        constants.ADVISORY_FORMAT_TOKENS, (AdvisoryDefault, AdvisoryIOS)))

def advisory_factory(adv_data, adv_format, logger):
    """Converts json into a list of advisory objects.
    :param adv_data: A dictionary describing an advisory.
    :param adv_format: The target format in ('default', 'ios')
    :param logger: A logger (for now expecting to be ready to log)
    :returns advisory instance according to adv_format
    """
    adv_map = {}  # Initial fill from shared common model key map:
    for k, v in ADVISORIES_COMMONS_MAP.items():
        adv_map[k] = adv_data[v]


    if adv_format == constants.DEFAULT_ADVISORY_FORMAT_TOKEN:
        for k, v in IPS_SIG_MAP.items():
            adv_map[k] = adv_data[v]
    else:  # IOS advisory format targeted:
        for k, v in IOS_ADD_ONS_MAP.items():
            adv_map[k] = adv_data[v]

    an_adv = advisory_format_factory_map()[adv_format](**adv_map)
    logger.debug(
        "{} Advisory {} Created".format(adv_format, an_adv.advisory_id))

    return an_adv
