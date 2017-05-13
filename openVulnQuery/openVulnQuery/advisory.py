from abc import ABCMeta


class Filterable(object):
    """Filterable mixin class"""

    def filter(self, *args):
        filtered_dict = {}
        for arg in args:
            if hasattr(self, arg):
                attr = getattr(self, arg)
                if isinstance(attr, list) and attr and isinstance(attr[0], Filterable):
                    filtered_dict[arg] = [a.filter(*args) for a in attr]
                else:
                    filtered_dict[arg] = attr
        return filtered_dict


class Advisory(Filterable):
    """Abstract Advisory object"""

    __metaclass__ = ABCMeta

    def __init__(self, advisory_id, sir, first_published, last_updated, cves,
                 bug_ids, cvss_base_score, advisory_title, publication_url, cwe,
                 product_names, summary, ips_signatures):
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
        self.ips_signatures = [IPSSignature(**kwargs) if not isinstance(kwargs, basestring) else "NA" for kwargs in ips_signatures]


class CVRF(Advisory):
    """CVRF object inherits from Advisory"""

    def __init__(self, *args, **kwargs):
        self.cvrf_url = kwargs.pop('cvrf_url', None)
        super(CVRF, self).__init__(*args, **kwargs)


class OVAL(Advisory):
    """OVAL object as an Advisory"""

    def __init__(self, *args, **kwargs):
        self.oval_url = kwargs.pop('oval_url', None)
        super(OVAL, self).__init__(*args, **kwargs)


class AdvisoryIOS(Advisory):
    """Advisory Object with additional information on IOS/IOSXE version """

    def __init__(self, *args, **kwargs):
        self.first_fixed = kwargs.pop('first_fixed', None)
        self.ios_release = kwargs.pop('ios_release', None)
        self.oval_url = kwargs.pop('oval_url', None)
        self.cvrf_url = kwargs.pop('cvrf_url', None)
        super(AdvisoryIOS, self).__init__(*args, **kwargs)


class IPSSignature(Filterable):

    def __init__(self, legacyIpsId, releaseVersion, softwareVersion, legacyIpsUrl):
        self.legacy_ips_id = legacyIpsId
        self.release_version = releaseVersion
        self.software_version = softwareVersion
        self.legacy_ips_url = legacyIpsUrl


