from abc import ABCMeta
from platform import python_version_tuple as p_v_t

import constants
__is_future_version = False if int(p_v_t()[0]) < 3 else True

# noinspection PyCompatibility
base_str = (str, bytes, bytearray) if __is_future_version else basestring

NA = constants.NA_INDICATOR
IPS_SIG = constants.IPS_SIGNATURE_LABEL


class Filterable(object):
    """Filterable mixin class"""

    def filter(self, *args):
        filtered_dict = {}
        for arg in args:
            if hasattr(self, arg):
                attr = getattr(self, arg)
                if all([isinstance(attr, list),  # A list
                        attr,  # Not empty
                        isinstance(attr[0], Filterable)  # First is our 'type'
                        ]):
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


class CVRF(Advisory):
    """CVRF object inherits from Advisory"""

    def __init__(self, *args, **kwargs):
        self.cvrf_url = kwargs.pop('cvrf_url')
        self.ips_signatures = []
        if IPS_SIG in kwargs:
            self.ips_signatures = [
                IPSSignature(**kw) if not isinstance(kw, base_str) else NA
                for kw in kwargs.pop(IPS_SIG)]
        super(CVRF, self).__init__(*args, **kwargs)


class OVAL(Advisory):
    """OVAL object as an Advisory"""

    def __init__(self, *args, **kwargs):
        self.oval_url = kwargs.pop('oval_url')
        self.ips_signatures = []
        if IPS_SIG in kwargs:
            self.ips_signatures = [
                IPSSignature(**kw) if not isinstance(kw, base_str) else NA
                for kw in kwargs.pop(IPS_SIG)]
        super(OVAL, self).__init__(*args, **kwargs)


class AdvisoryIOS(Advisory):
    """Advisory Object with additional information on IOS/IOSXE version """

    def __init__(self, *args, **kwargs):
        self.first_fixed = kwargs.pop('first_fixed')
        self.ios_release = kwargs.pop('ios_release')
        self.oval_url = kwargs.pop('oval_url')
        self.cvrf_url = kwargs.pop('cvrf_url')
        super(AdvisoryIOS, self).__init__(*args, **kwargs)


class IPSSignature(Filterable):
    def __init__(self, legacyIpsId, releaseVersion, softwareVersion,
                 legacyIpsUrl):
        self.legacy_ips_id = legacyIpsId
        self.release_version = releaseVersion
        self.software_version = softwareVersion
        self.legacy_ips_url = legacyIpsUrl


def advisory_factory(adv_data, adv_format, logger):
    """Converts json into a list of advisory objects.
    :param adv_data: A dictionary describing an advisory.
    :param adv_format: The target format in ('cvrf', 'oval', 'ios')
    :param logger: A logger (for now expecting to be ready to log)
    :returns advisory instance according to adv_format
    """
    if adv_format not in ('cvrf', 'opal', 'ios'):
        raise ValueError(
            "Format {} not implemented in advisories".format(adv_format))

    advisory_factory_map = {
        'cvrf': CVRF,
        'opal': OVAL,
        'ios': AdvisoryIOS,
    }

    adv = adv_data
    adv_map = {
        'advisory_id': adv_data["advisoryId"],
        'sir': adv_data["sir"],
        'first_published': adv_data["firstPublished"],
        'last_updated': adv_data["lastUpdated"],
        'cves': adv_data["cves"],
        # Empty Union Variant Slot x_url
        'bug_ids': adv_data["bugIDs"],
        'cvss_base_score': adv_data["cvssBaseScore"],
        'advisory_title': adv_data["advisoryTitle"],
        'publication_url': adv_data["publicationUrl"],
        'cwe': adv_data["cwe"],
        'product_names': adv_data["productNames"],
        'summary': adv_data["summary"],
        # Pending Variant Slot ips or x_fixed/x_release

    }
    if adv_format == 'cvrf':
        adv_map['cvrf_url'] = adv_data["cvrfUrl"]  # Variant::Union
        # cvrf and oval only attributes:
        adv_map[IPS_SIG] = adv_data["ipsSignatures"]
    else:  # implicit 'ios' flavor/format
        if 'oval' in adv_data:
            oval_url = adv_data['oval']
        else:
            oval_url = adv_data['ovalUrl']
        if adv_format == "oval":
            adv_map['oval_url'] = oval_url  # Variant::Union
            # cvrf and oval only attributes:
            adv_map['ips_signatures'] = adv_data["ipsSignatures"]
        else:  # TODO, was 'if not adv_format:', verify that OK
            adv_map['oval_url'] = oval_url  # Variant::Union
            # neither cvrf nor oval only attributes:
            adv_map['first_fixed'] = adv_data["firstFixed"]
            adv_map['ios_release'] = adv_data["iosRelease"]

    an_adv = advisory_factory_map[adv_format](**adv_map)
    logger.debug(
        "{} Advisory {} Created".format(adv_format, an_adv.advisory_id))

    return an_adv
