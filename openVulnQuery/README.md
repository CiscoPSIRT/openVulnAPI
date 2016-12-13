#openVulnQuery
A python-based module(s) to query the Cisco PSIRT openVuln API.

The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). More information about the API can be found at: https://developer.cisco.com/site/PSIRT/

####PIP Installation
- pip install openVulnQuery

  If you are experiencing any difficulty installing openVulnQuery.
  Here is the link to [common installation issues solutions]   (https://github.com/iamparas/openVulnAPI/blob/master/openVulnQuery/InstallationIssueSolutions.md).

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
        >> python main.py --cvrf --all
        >> python main.py --oval --all

--advisory
        Search by specific advisory id
        Examples:
        >> python main.py --cvrf --advisory cisco-sa-20110201-webex
        >> python main.py --oval --advisory cisco-sa-20100324-ldp

--cve
        Search by specific cve id
        Examples:
        >> python main.py --cvrf --cve CVE-2010-3043
        >> python main.py --oval --cve CVE-2010-0576

--latest
        Search by the number of latest advisories in cvrf or oval format
        Examples:
        >> python main.py --cvrf --latest 10
        >> python main.py --oval --latest 10

        Note: the latest option is limited to 100 maximum queries

--severity
        Search by severity (low, medium, high, critical)
        Note: Oval does not have a low severity
        Examples:
        >> python main.py --cvrf --severity critical
        >> python main.py --cvrf --severity high
        >> python main.py --cvrf --severity medium
        >> python main.py --cvrf --severity low
        >> python main.py --oval --severity critical
        >> python main.py --oval --severity high
        >> python main.py --oval --severity medium

--year
        Search by the year (1995 to present)
        Examples:
        >> python main.py --cvrf --year 2016
        >> python main.py --oval --year 2016
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
              python main.py --cvrf or --oval --any API filter -f  or --fields list of fields separated by space
              >> python main.py --cvrf --all -f sir cves cvrf_url
              >> python main.py --cvrf --severity critical -f last_updated cves
              >> python main.py --oval --all -f sir cves oval_url
              >> python main.py --oval --severity critical -f last_updated cves

        CVRF XML Fields
              Examples:
              python main.py --cvrf --any API filter -f or --fields list of fields separated by space
              >> python main.py --cvrf --all -f bug_ids vuln_title product_names
              >> python main.py --cvrf --severity critical -f bug_ids summary

        Combination
              Examples:
              python main.py --cvrf --any API filter -f or --fields list of fields separated by space
              >> python main.py --cvrf --all -f sir bug_ids cves vuln_title
              >> python main.py --cvrf --year 2011 -f cves cvrf_url bug_ids summary product_names
```
####Output Format (Optional)
```
Default
        Table style printed to screen
        Example:
        >> python main.py --cvrf --year 2016

--json file path
        Returns json in a file in the specified path
        Example:
        >> python main.py --cvrf --year 2016 --json  /Users/bkorabik/Documents/2016_cvrf.json

--csv file path
        Creates a CSV file in the specified path
        Example:
        >> python main.py --cvrf --year 2016 --csv  /Users/bkorabik/Documents/2016_cvrf.csv
```
####Count (Optional)
Returns the count of fields entered with -f or --fields. If no fields are entered the base API fields are counted and displayed
```
-c

        Examples:
        >> python main.py --cvrf --year 2016 -c
        >> python main.py --cvrf --severity low -f sir cves bug_ids -c
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
        >> python main.py --cvrf --year 2013 -f sir | grep -c "Critical"
        >> python main.py --cvrf --severity critical -f first_published | grep -c "2013"
```

If more than one API filter is entered, the last filter will be used for the API call

####Run OpenVulnQuery as a Library
<<<<<<< HEAD
After you install openVulnQuery package, you can use the query_client module to make API-call which returns 
 advisory objects. For each query to the API, you can pick the advisory format. 
```
>> from openVulnQuery import query_client
>> query_client = query_client.QueryClient(client_id = "", client_secret = "")
>> advisories = query_client.get_by_year(year = 2010, adv_format = "cvrf")
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
=======
After you install openVulnQuery package, you can use the query_client module to make API-call which returns
 advisory objects. For each query to the API, you can pick advisory format and whether you want to parse the cvrf as we only support parsing cvrf xml files right now.
```
>> from openVulnQuery import query_client
>> query_client = query_client.OpenVulnQueryClient(client_id='', client_secret='')
>> advisories = query_client.get_by_year(year=2010, adv_format = 'cvrf', cvrf_parsed = True)
```
Here are the information stored in advisory object.
#####Advisory
      * SIR
      * First Published
      * Last Updated
      * CVES
      * CVRF / OVAL URL

       Cvrf
          * Document Title
          * Summary
          * Publication URL
          * Full Product Name
          * List of Vulnerabilities

              Vulnerability
                * Title
                * CVE
                * BUG Ids
                * Base Score
>>>>>>> upstream/master
