from abc import ABCMeta


class Advisory(object):
    """Abstract Advisory object"""

    __metaclass__ = ABCMeta

    def __init__(self, advisory_id, sir, first_published, last_updated, cves,
                 bug_ids, cvss_base_score, advisory_title, publication_url, cwe,
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

    def filter(self, *args):
        """Returns arg and value as a dictionary"""
        return {arg: getattr(self, arg)
                      for arg in args
                         if hasattr(self, arg)}


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
