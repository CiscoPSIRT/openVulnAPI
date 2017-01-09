#openVulnQuery
A python-based module(s) to query the Cisco PSIRT openVuln API.

The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). More information about the API can be found at: https://developer.cisco.com/site/PSIRT/

####PIP Installation
- pip install openVulnQuery

####Requirements
- Tested on Python Version 2.7
- argparse 1.4.0
- PrettyTable 0.7.2
- requests 2.10.0
- lxml 3.6.0

####Config File
Obtain client ID and Secret:

1. https://apiconsole.cisco.com/
2. Sign In
3. My Applications Tab
4. Register a New Application
  - Name
  - Under OAuth2.0 Credentials check Client Credentials
  - Under Select APIs choose Cisco PSIRT openVuln API
  - Agree to the terms and service and click Register
  - Edit CLIENT_ID and CLIENT_SECRET in the config file with the ones provided from the steps above.
  - To edit the config.py file if installing with pip, run the command pip show openVulnQuery and cd into the location of the package. Then cd into the openVulnQuery folder and open the config.py file in your favorite editor, modify and save.
  - OAuth2 Token automatically generated on each call to the API.

####Run OpenVulnQuery in the Terminal
- If installed with pip run the program by typing
```
  >>OpenVulnQuery --Advisory Type --API Filters --Parsing Fields --Output Format -Count
```
- Or cd into the directory with the main.py file and run using
```
  >>python main.py --Advisory Type --API Filters --Parsing Fields --Output Format -Count
```
Notes:

-- Used for whole word commands, - Used for single character commands

####Advisory Type (Required)
```
--cvrf
        Filter openVuln API by only cvrf advisories
--oval
        Filter openVuln API by only oval advisories
```
####API Filters (Required)
```
--all
        Return all advisories in cvrf or oval format
        Examples:
        >> openVulnQuery --cvrf --all
        >> openVulnQuery --oval --all

--advisory
        Search by specific advisory id
        Examples:
        >> openVulnQuery --cvrf --advisory cisco-sa-20110201-webex
        >> openVulnQuery --oval --advisory cisco-sa-20100324-ldp

--cve
        Search by specific cve id
        Examples:
        >> openVulnQuery --cvrf --cve CVE-2010-3043
        >> openVulnQuery --oval --cve CVE-2010-0576

--latest
        Search by the number of latest advisories in cvrf or oval format
        Examples:
        >> openVulnQuery --cvrf --latest 10
        >> openVulnQuery --oval --latest 10

--severity
        Search by severity (low, medium, high, critical)
        Note: Oval does not have a low severity
        Examples:
        >> openVulnQuery --cvrf --severity critical
        >> openVulnQuery --cvrf --severity high
        >> openVulnQuery --cvrf --severity medium
        >> openVulnQuery --cvrf --severity low
        >> openVulnQuery --oval --severity critical
        >> openVulnQuery --oval --severity high
        >> openVulnQuery --oval --severity medium

--year
        Search by the year (1995 to present)
        Examples:
        >> openVulnQuery --cvrf --year 2016
        >> openVulnQuery --oval --year 2016

--product
         Search by the product name
         Examples:
         >> openVulnQuery --cvrf --product Cisco
         >> openVulnQuery --oval --product Cisco

--ios_xe 
        Search by IOS XE version
        Examples:
        >> openVulnQuery --cvrf --ios_xe 13.16.1S
        >> openVulnQuery --oval --ios_xe 13.16.1S
```
####Parsing Fields (Optional)
Notes:

If no fields are passed in the default API fields will be returned

Any field that has no information will return with with the field name and NA

##### Parsable Fields
  - advisory_id
  - sir
  - first_published
  - last_updated
  - cves
  - bug_ids
  - cvss_base_score
  - advisory_title
  - publication_url
  - cwe
  - product_names
  - summary
  - vuln_title
  - oval_urls
  - cvrf_url

```
-f or --fields

        API Fields
              Examples:
              openVulnQuery --cvrf or --oval --any API filter -f  or --fields list of fields separated by space
              >> openVulnQuery --cvrf --all -f sir cves cvrf_url
              >> openVulnQuery --cvrf --severity critical -f last_updated cves
              >> openVulnQuery --oval --all -f sir cves oval_url
              >> openVulnQuery --oval --severity critical -f last_updated cves

        CVRF XML Fields
              Examples:
              openVulnQuery --cvrf --any API filter -f or --fields list of fields separated by space
              >> openVulnQuery --cvrf --all -f bug_ids vuln_title product_names
              >> openVulnQuery --cvrf --severity critical -f bug_ids summary

        Combination
              Examples:
              openVulnQuery --cvrf --any API filter -f or --fields list of fields separated by space
              >> openVulnQuery --cvrf --all -f sir bug_ids cves vuln_title
              >> openVulnQuery --cvrf --year 2011 -f cves cvrf_url bug_ids summary product_names
```

#####Additional Filters
User can be more specific on filtering advisories when searching all advisories or by severity. They can filter based on last updated and first published dates providing start and end date as a search range. Dates should be entered in YYYY-MM-DD format. 
```
>> openVulnQuery --cvrf --severity high --last_updated 2016-01-02:2016-04-02 --json filename.json
>> openVulnQuery --cvrf --all --last_updated 2016-01-02:2016-07-02
>> openVulnQuery --cvrf --severity critical --first_published 2015:01:02:2015-01-01
```

####Output Format (Optional)
```
Default
        Table style printed to screen
        Example:
        >> openVulnQuery --cvrf --year 2016

--json file path
        Returns json in a file in the specified path
        Example:
        >> openVulnQuery --cvrf --year 2016 --json  /Users/bkorabik/Documents/2016_cvrf.json

--csv file path
        Creates a CSV file in the specified path
        Example:
        >> openVulnQuery --cvrf --year 2016 --csv  /Users/bkorabik/Documents/2016_cvrf.csv
```
####Count (Optional)
Returns the count of fields entered with -f or --fields. If no fields are entered the base API fields are counted and displayed
```
-c

        Examples:
        >> openVulnQuery --cvrf --year 2016 -c
        >> openVulnQuery --cvrf --severity low -f sir cves bug_ids -c
```

####Developers
- Update the config.py file with client id and secret
- Directly interact with query_client.py to query the Open Vuln API
- query_client.py returns Advisory Object 
- advisory.py module has Advisory object a abstract class which is inherited by CVRF and OVAL data type
- This abstraction hides the implementation details and the data source used to populate the data type. The data members of CVRF and OVAL advisories are populated from API results as well parsing the XML file obtained from the API results. 

####Disclosures:
No support for filtering based on --API fields, you can't use --year 2016 and --severity high

Filtering with Grep:
```
Finding the Number of CVRF Advisories with a "Critical" sir in 2013
        >> openVulnQuery --cvrf --year 2013 -f sir | grep -c "Critical"
        >> openVulnQuery --cvrf --severity critical -f first_published | grep -c "2013"
```

If more than one API filter is entered, the last filter will be used for the API call

####Run OpenVulnQuery as a Library
After you install openVulnQuery package, you can use the query_client module to make API-call which returns 
 advisory objects. For each query to the API, you can pick the advisory format. 
```
>> from openVulnQuery import query_client
>> query_client = query_client.QueryClient(client_id = "", client_secret = "")
>> advisories = query_client.get_by_year(year = 2010, adv_format = "cvrf")
```
If you want to use the additional date filters based on first published and last updated date. You can pass the appropriate class
```
>> advisories = query_client.get_by_severity(adv_format="cvrf", severity="high", FirstPublished(2016-01-01, 2016-02-02))
>> advisories = query_client.get_by_severity(adv_format="oval", severity="low", LastUpdated(2016-01-01, 2016-02-02))
```

Here are the information stored in advisory object.
#####Advisory
      * advisory_id
      * sir
      * first_published
      * last_updated
      * cves
      * bug_ids
      * cvss_base_score
      * advisory_title
      * publication_url
      * cwe
      * product_names
      * summary
      
   #####CVRF (inherits Advisory Abstract Class)
            * cvrf_url
            * vuln_title
   #####OVAL (inherits Advisory Advisory Class)
            * oval_url