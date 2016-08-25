from lxml import etree
import urllib2
import cStringIO
import logging

class Advisory(object):
    """Creates an Advisory object"""

    def __init__(self, advisory_dict, parse_cvrf, adv_format):
        self.parse_cvrf = parse_cvrf
        self.adv_format = adv_format
        self.sir = advisory_dict["sir"]
        self.advisory_id = advisory_dict["advisoryId"]
        self.first_published = advisory_dict["firstPublished"]
        self.last_updated = advisory_dict["lastUpdated"]
        self.cves = advisory_dict["cves"]
        self._cvrf = None
        if self.adv_format == "cvrf":
            self.cvrf_url = advisory_dict["cvrfUrl"]
        else:
            self.oval_urls = advisory_dict["oval"]

    @property
    def cvrf(self):
        if self.parse_cvrf and not self._cvrf:
            self._cvrf = Cvrf.fromXML(self.cvrf_url)
        return self._cvrf


class Cvrf(object):
    """Creates an Cvrf object mapped from given XML"""

    def __init__(self, document_title, summary, publication_url,
                 full_product_name_list, vuln_list):
        self.document_title = document_title
        self.summary = summary
        self.publication_url = publication_url
        self.full_product_name_list = full_product_name_list
        self.vuln_list = [Vulnerability(**vuln_args) for vuln_args in vuln_list]


    @classmethod
    def fromXML(cls, xml_url):
        """Parses XML to prepare arguments for CVRF object"""

        xml = Cvrf.from_url(xml_url)
        bad_xml = xml.decode("utf-8", errors="ignore")
        good_xml = bad_xml.encode("utf-8")
        tree = etree.parse(cStringIO.StringIO(good_xml))
        vuln_args = []
        vulnerability = Cvrf.get_elem(tree, "vuln_ns:Vulnerability")
        for i, r in enumerate(vulnerability, start=1):
            #Multiple BugIds are stored in Note under Vulnerabilities for latest cvrf 1.1 advisories
            bug_ids = Cvrf.get_text(tree, "vuln_ns:Vulnerability[%s]/vuln_ns:Notes/vuln_ns:Note[@Title='Cisco Bug IDs']" % i)
            if  bug_ids == "NA":
                bug_ids = Cvrf.get_text(tree, "vuln_ns:Vulnerability[%s]/vuln_ns:ID" % i)
            #multiple vulnerabilities are seperated by ordinal number
            arg = {"title" : Cvrf.get_text(tree, "vuln_ns:Vulnerability[%s]/vuln_ns:Title" % i),
                   "cve" : Cvrf.get_text(tree, "vuln_ns:Vulnerability[%s]/vuln_ns:CVE" % i),
                   "bug_ids" : bug_ids.split(","),
                   "base_score" : Cvrf.get_text(tree, "vuln_ns:Vulnerability[%s]/vuln_ns:CVSSScoreSets/vuln_ns:ScoreSet/vuln_ns:BaseScore" % i)}
            vuln_args.append(arg)

        kwargs = {
                "document_title" : Cvrf.get_text(tree, "cvrf_ns:DocumentTitle"),
                "summary" : Cvrf.get_text(tree, "cvrf_ns:DocumentNotes/cvrf_ns:Note"),
                "publication_url" : Cvrf.get_text(tree, "cvrf_ns:DocumentReferences/cvrf_ns:Reference/cvrf_ns:URL"),
                "full_product_name_list" : Cvrf.get_text(tree, "prod_ns:ProductTree/prod_ns:FullProductName"),
                "vuln_list" : vuln_args
            }
        return cls(**kwargs)

    @staticmethod
    def from_url(url):
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

    @staticmethod
    def get_elem(tree, path):
        """Returns node element in parsed xml pointed by xpath"""

        cvrf_ns = "http://www.icasi.org/CVRF/schema/cvrf/1.1"
        prod_ns =  "http://www.icasi.org/CVRF/schema/prod/1.1"
        vuln_ns = "http://www.icasi.org/CVRF/schema/vuln/1.1"
        result = tree.xpath("/cvrf_ns:cvrfdoc/%s" % path,
                            namespaces = {"cvrf_ns" : cvrf_ns,
                                          "prod_ns" : prod_ns,
                                          "vuln_ns" : vuln_ns})
        return result

    @staticmethod
    def get_text(tree, path):
        """Returns text value in parsed xml pointed by xpath"""

        elems = Cvrf.get_elem(tree, path)
        if len(elems) == 0:
            return "NA"
        if len(elems) == 1:
            return elems.pop().text
        return [e.text for e in elems]

class Vulnerability(object):
    """Creates an Vulnerability Object"""

    def __init__(self, title, cve, bug_ids, base_score):
        self.vuln_title = title
        self.vuln_cve = cve
        self.vuln_bug_ids = bug_ids
        self.vuln_base_score = base_score
