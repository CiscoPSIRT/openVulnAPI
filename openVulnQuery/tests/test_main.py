import unittest
import mock
import sys
sys.path.append("openVulnQuery")
import main
import advisory_object

class MainTest(unittest.TestCase):

    def test_xml_parse_needed(self):
        # API Fields
        adv_format = "cvrf"
        fields = ['sir', 'cves']
        parse_xml = main.xml_parse_needed(adv_format, fields)
        self.assertEqual(parse_xml, False)

        # API + VULN Fields
        adv_format = "cvrf"
        fields = ['last_updated', 'vuln_title']
        parse_xml = main.xml_parse_needed(adv_format, fields)
        self.assertEqual(parse_xml, True)

        # API + CVRF Fields
        fields = ['advisory_id', 'publication_url']
        parse_xml = main.xml_parse_needed(adv_format, fields)
        self.assertEqual(parse_xml, True)

        # API + CVRF + VULN Fields
        fields = ['sir', 'document_title', 'vuln_bug_ids']
        parse_xml = main.xml_parse_needed(adv_format, fields)
        self.assertEqual(parse_xml, True)

        # CVRF + VULN Fields
        fields = ['summary', 'vuln_title']
        parse_xml = main.xml_parse_needed(adv_format, fields)
        self.assertEqual(parse_xml, True)

    def test_filter_entered_fields(self):
        # API Fields
        fields = ['test', 'sir', 'first_published', 'invalid']
        api_fields, cvrf_fields, vuln_fields = main.filter_entered_fields(fields)
        self.assertEqual(api_fields, ['sir', 'first_published'])
        self.assertEqual(cvrf_fields, [])
        self.assertEqual(vuln_fields, [])

        # API + VULN Fields
        fields = ['last_updated', 'invalid', 'vuln_title']
        api_fields, cvrf_fields, vuln_fields = main.filter_entered_fields(fields)
        self.assertEqual(api_fields, ['last_updated'])
        self.assertEqual(cvrf_fields, [])
        self.assertEqual(vuln_fields, ['vuln_title'])

        # API + CVRF Fields
        fields = ['invalid', 'advisory_id', 'publication_url']
        api_fields, cvrf_fields, vuln_fields = main.filter_entered_fields(fields)
        self.assertEqual(api_fields, ['advisory_id'])
        self.assertEqual(cvrf_fields, ['publication_url'])
        self.assertEqual(vuln_fields, [])

        # API + CVRF + VULN Fields
        fields = ['sir', 'test', 'document_title', 'test', 'vuln_bug_ids']
        api_fields, cvrf_fields, vuln_fields = main.filter_entered_fields(fields)
        self.assertEqual(api_fields, ['sir'])
        self.assertEqual(cvrf_fields, ['document_title'])
        self.assertEqual(vuln_fields, ['vuln_bug_ids'])

        # CVRF + VULN Fields
        fields = ['test', 'summary', 'vuln_title', 'test']
        api_fields, cvrf_fields, vuln_fields = main.filter_entered_fields(fields)
        self.assertEqual(api_fields, [])
        self.assertEqual(cvrf_fields, ['summary'])
        self.assertEqual(vuln_fields, ['vuln_title'])

    def test_map_vulnerabilites_to_advisory(self):
        # Test with Vuln Data
        advisories = [{'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCuw64516'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCur27459'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'NA'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCsb12598'}, {'vuln_bug_ids': 'CSCsb40304'}, {'vuln_bug_ids': 'CSCsd92405'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'NA'}, {'vuln_bug_ids': 'NA'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCef90002'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCsb25337'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCek37177'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'CSCsf28840'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'NA'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'NA'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'NA'}]},
                      {'sir': u'Low', 'vulns': [{'vuln_bug_ids': 'NA'}]}]
        updated_advisories = main.map_vulnerabilites_to_advisory(advisories)
        updated_advisories_output = [{'sir': u'Low', 'vuln_bug_ids': 'CSCuw64516'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCur27459'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCsb12598'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCsb40304'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCsd92405'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCef90002'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCsb25337'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCek37177'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'CSCsf28840'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'},
                                     {'sir': u'Low', 'vuln_bug_ids': 'NA'}]
        self.assertEqual(updated_advisories, updated_advisories_output)

        # Test without Vuln Data
        advisories = [{'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'},
                      {'sir': u'Low'}]
        updated_advisories = main.map_vulnerabilites_to_advisory(advisories)
        updated_advisories_output = [{'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'},
                                     {'sir': u'Low'}]
        self.assertEqual(updated_advisories, updated_advisories_output)

    def test_convert_list_to_string(self):
        field_list = {'sir' : 'low', 'cves' : ["CVE1", "CVE2", "CVE3"]}
        convert_list_to_string = main._convert_list_to_string(field_list)
        self.assertEqual(convert_list_to_string, {'sir': 'low', 'cves': 'CVE1    CVE2    CVE3'})

    def test_count_field(self):
        # Test count with list
        advisory_field = [u'CVE-2007-2033', u'CVE-2007-2035']
        count = main.count_field(advisory_field)
        self.assertEqual(count, 2)

        # Test count with string
        advisory_field = "Low"
        count = main.count_field(advisory_field)
        self.assertEqual(count, 1)

    def test_create_api_advisory_object(self):
        advisory = {u'sir': u'Low',
                    u'cvrfUrl': u'http://tools.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/cisco-sa-20151210-tvcs/cvrf/cisco-sa-20151210-tvcs_cvrf.xml',
                    u'lastUpdated': u'2015-12-10T06:00:00+0000',
                    u'firstPublished': u'2015-12-10T06:00:00+0000',
                    u'advisoryId': u'cisco-sa-20151210-tvcs',
                    u'cves': [u'CVE-2015-6414']}
        cvrf_parsed = False
        adv_format = 'cvrf'
        adv_object = advisory_object.Advisory(advisory, cvrf_parsed, adv_format)
        return [adv_object]

    def mock_XML():
        document_title = "Document Title"
        summary = "Summary"
        publication_url = "https://www.cisco.com"
        full_product_name_list = ["Product 1", "Product 2"]
        vuln_list = [{"title" : "Vuln Title", "cve" : "CVE123", "bug_ids" : ["ID1", "ID2"], "base_score" : "7.0"}]
        return advisory_object.Cvrf(document_title, summary, publication_url, full_product_name_list, vuln_list)

    @mock.patch('advisory_object.Cvrf.fromXML', side_effect=mock_XML)
    def test_create_xml_advisory_object(self, mock_xml):
        advisory = {u'sir': u'Low',
                    u'cvrfUrl': u'http://tools.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/cisco-sa-20151210-tvcs/cvrf/cisco-sa-20151210-tvcs_cvrf.xml',
                    u'lastUpdated': u'2015-12-10T06:00:00+0000',
                    u'firstPublished': u'2015-12-10T06:00:00+0000',
                    u'advisoryId': u'cisco-sa-20151210-tvcs',
                    u'cves': [u'CVE-2015-6414']}
        cvrf_parsed = True
        adv_format = 'cvrf'
        adv_object = advisory_object.Advisory(advisory, cvrf_parsed, adv_format)
        return [adv_object]

    def test_parse_advisory_objects(self):
        # Parse Advisory Object with API Data
        advisory = self.test_create_api_advisory_object()
        api_fields = ["sir", "cvrf_url"]
        cvrf_fields = []
        vuln_fields = []
        parsed_object = main.parse_advisory_objects(advisory, api_fields, cvrf_fields, vuln_fields)
        result = ({'sir': 1, 'cvrf_url': 1},
                 [{'sir': u'Low', 'cvrf_url': u'http://tools.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/cisco-sa-20151210-tvcs/cvrf/cisco-sa-20151210-tvcs_cvrf.xml'}])
        self.assertEqual(parsed_object, result)

        # Parse Advisory Object with API and XML Data
        advisory = self.test_create_xml_advisory_object()
        api_fields = ["cves", "sir"]
        cvrf_fields = ["publication_url"]
        vuln_fields = ["vuln_title"]
        parsed_object = main.parse_advisory_objects(advisory, api_fields, cvrf_fields, vuln_fields)
        result = ({'vuln_title': 1, 'sir': 1, 'publication_url': 1, 'cves': 1},
                 [{'vulns': [{'vuln_title': 'Cisco TelePresence Video Communication Server Information Disclosure Vulnerability'}],
                 'sir': u'Low',
                 'publication_url': 'http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20151210-tvcs',
                 'cves': [u'CVE-2015-6414']}])
        self.assertEqual(parsed_object, result)
