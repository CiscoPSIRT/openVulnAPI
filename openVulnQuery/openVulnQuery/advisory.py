from abc import ABCMeta, abstractmethod
from lxml import etree
import urllib2
import cStringIO
import logging


def from_url(url):
    """Helper method to get html from url"""
    while True:
        try:
            r = urllib2.urlopen(url)
        except URLError as e:
            if hasattr(e, 'reason'):
                logging.error("We failed to reach server")
                logging.error("Reason : ", e.reason)
            elif hasattr(e, 'code'):
                logging.error("Server couldn't fulfill the request")
                logging.error(e.code)
        else:
            xml = r.read()
        if xml:
            break
    return xml


def get_elem(tree, path):
    """Helper method to extract node element in  xml by xpath"""

    cvrf_ns = "http://www.icasi.org/CVRF/schema/cvrf/1.1"
    prod_ns =  "http://www.icasi.org/CVRF/schema/prod/1.1"
    vuln_ns = "http://www.icasi.org/CVRF/schema/vuln/1.1"
    result = tree.xpath("/cvrf_ns:cvrfdoc/%s" % path,
                        namespaces = {"cvrf_ns" : cvrf_ns,
                                      "prod_ns" : prod_ns,
                                      "vuln_ns" : vuln_ns})
    return result


def get_text(tree, path):
    """Helper method to return text value in  xml pointed by xpath"""

    elems = get_elem(tree, path)
    if len(elems) == 0:
        return "NA"
    if len(elems) == 1:
        return elems.pop().text
    return [e.text for e in elems]

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

    def filter(*args):
        """Returns arg and value as a dictionary"""
        return {arg : getattr(self, arg)
                      for arg in args
                         if hasattr(self, arg)}

class CVRF(Advisory):
    """CVRF object inherits from Advisory"""

    def __init__(self, *args, **kwargs):
        self.cvrf_url = kwargs.pop('cvrf_url', None)
        self._additional_fields = None
        super(CVRF, self).__init__(*args, **kwargs)

    @property
    def additional_fields(self):
        if not self._additional_fields:
            self._additional_fields = CVRF.fromXML(self.cvrf_url)
        return self._additional_fields

    def __getattr__(self, attr):
        try:
            return self.additional_fields[attr]
        except:
            raise AttributeError("Attribute doesnot exist")

    @staticmethod
    def fromXML(xml_url):
        """Parses XML to prepare arguments for CVRF Advisory"""

        xml = from_url(xml_url)
        bad_xml = xml.decode("utf-8", errors="ignore")
        good_xml = bad_xml.encode("utf-8")
        tree = etree.parse(cStringIO.StringIO(good_xml))

        vulnerability = get_elem(tree, "vuln_ns:Vulnerability")
        vuln_title = []
        for i, r in enumerate(vulnerability, start=1):
            vuln_title.append(get_text(tree, "vuln_ns:Vulnerability[%s]/vuln_ns:Title" % i))
        kwargs = {
                "vuln_title" : vuln_title
            }
        return kwargs



class OVAL(Advisory):
    """OVAL object as an Advisory"""

    def __init__(self, *args, **kwargs):
        super(OVAL, self).__init__(*args, **kwargs)
