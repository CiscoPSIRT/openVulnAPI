# openVulnQuery
A python-based module(s) to query the Cisco PSIRT openVuln API.

The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). More information about the API can be found at: https://developer.cisco.com/site/PSIRT/discover/overview/

#### PIP Installation
- `pip install openVulnQuery`

  If you are experiencing any difficulty installing openVulnQuery.
  Here is the link to [common installation issues solutions]   (https://github.com/iamparas/openVulnAPI/blob/master/openVulnQuery/InstallationIssueSolutions.md).

Requirements
- Tested on Python Version 2.7.13
- `argparse >= 1.4.0`
- requests >= 2.10.0`

#### Config File
Obtain client ID and Secret:

1. Visit https://apiconsole.cisco.com/
2. Sign In
3. Select My Applications Tab
4. Register a New Application by:
   - Entering Application Name
   - Under OAuth2.0 Credentials check Client Credentials
   - Under Select APIs choose Cisco PSIRT openVuln API
   - Agree to the terms and service and click Register
5. Take note of the "rate contract" presented like e.g.:
    ```
    Rate Limits
    10	Calls per second
    5,000	Calls per day
    ```
6. Note the value of "Client ID" (a string like e.g. 'abc12abcd13abcdefabcde1a')
7. Note the value of "Client Secret" (a string like e.g. '1a2abcDEfaBcDefAbcDeFA3b')
8. Provide the credentials to the application at runtime via two preferred alternativev ways:
   * Either export two matching environment variables (below the syntax for bash and assuming the values are as in steps 6. and 7.):
        ```
        >> export CLIENT_ID="abc12abcd13abcdefabcde1a" 
        >> export CLIENT_SECRET="1a2abcDEfaBcDefAbcDeFA3b"
        ```
   * Or create a valid JSON file (e.g. `credentials.json`) with these personal credentials similar to the below given (assuming the values are as in steps 6. and 7.):
        ```
        {
            "CLIENT_ID": "abc12abcd13abcdefabcde1a", 
            "CLIENT_SECRET": "1a2abcDEfaBcDefAbcDeFA3b"
        }
        ```
9. Do not distribute the credentials file resulting from previous step

**Notes**: 
* The resulting OAuth2 Token will be automatically generated on every call to the API.

#### Run OpenVulnQuery in the Terminal
- If installed with pip run the program by typing
```
  >>OpenVulnQuery --config PathToCredentialsFile --Advisory Type --API Filters --Parsing Fields --Output Format -Count
```
- Or cd into the directory with the main.py file and run using
```
  >>python main.py --config PathToCredentialsFile --Advisory Type --API Filters --Parsing Fields --Output Format -Count
```
Notes:

-- Used for whole word commands, - Used for single character commands

#### Configuration (Optional)
```
--config FILE
        Path to JSON file with credentials (as in above step 8)
        A sample has been provided in the same folder as main.py:
            sample:configuration.json
        The configuration will be tried first from config file, 
        next from environemnt variables CLIENT_ID and CLIENT_SECRET,
        last from config.py variable values, or fail.
```

#### Advisory Type (Required)
```
--cvrf
        Filter openVuln API by only cvrf advisories
--oval
        Filter openVuln API by only oval advisories
```
#### API Filters (Required)
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

        Note: the latest option is limited to 100 maximum queries

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

--ios
        Search by IOS version
        Examples:
        >> openVulnQuery --ios 15.6\(2\)SP  (*use \ to escape bracket in ios version)
        >> openVulnQuery --ios 15.6(\2\)SP


--ios_xe
        Cisco IOS Software Checker has been integrated with openVulnAPI.
        Search by Cisco IOS or Cisco IOS XE Software version.
        Example:
        >> openVulnQuery --ios_xe 3.16.1S

```

#### Client Application (Optional)
```
--user-agent APPLICATION
        Name of application to be sent as User-Agent header value in the request.
        Default is TestApp.
```

#### Parsing Fields (Optional)
Notes:

If no fields are passed in the default API fields will be returned

Any field that has no information will return with with the field name and NA

##### Available Fields
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
              openVulnQuery --config PathToCredentialsFile --cvrf or --oval --any API filter -f  or --fields list of fields separated by space
              >> openVulnQuery --config PathToCredentialsFile --cvrf --all -f sir cves cvrf_url
              >> openVulnQuery --config PathToCredentialsFile --cvrf --severity critical -f last_updated cves
              >> openVulnQuery --config PathToCredentialsFile --oval --all -f sir cves oval_url
              >> openVulnQuery --config PathToCredentialsFile --oval --severity critical -f last_updated cves

        CVRF XML Fields
              Examples:
              openVulnQuery --config PathToCredentialsFile --cvrf --any API filter -f or --fields list of fields separated by space
              >> openVulnQuery --config PathToCredentialsFile --cvrf --all -f bug_ids vuln_title product_names
              >> openVulnQuery --config PathToCredentialsFile --cvrf --severity critical -f bug_ids summary

        Combination
              Examples:
              openVulnQuery --config PathToCredentialsFile --cvrf --any API filter -f or --fields list of fields separated by space
              >> openVulnQuery --config PathToCredentialsFile --cvrf --all -f sir bug_ids cves vuln_title
              >> openVulnQuery --config PathToCredentialsFile --cvrf --year 2011 -f cves cvrf_url bug_ids summary product_names
```

##### Additional Filters
User can be more specific on filtering advisories when searching all advisories or by severity. They can filter based on last updated and first published dates providing start and end date as a search range. Dates should be entered in YYYY-MM-DD format.
```
>> # export CLIENT_ID and CLIENT_SECRET or write to config.py ... then:
>> openVulnQuery --cvrf --severity high --last_updated 2016-01-02:2016-04-02 --json filename.json
>> openVulnQuery --cvrf --all --last_updated 2016-01-02:2016-07-02
>> openVulnQuery --cvrf --severity critical --first_published 2015-01-02:2015-01-04
```

#### Output Format (Optional)
```
Default
        Table style printed to screen
        Example:
        >> openVulnQuery --config PathToCredentialsFile --cvrf --year 2016

--json file path
        Returns json in a file in the specified path
        Example:
        >> openVulnQuery --config PathToCredentialsFile --cvrf --year 2016 --json  /Users/bkorabik/Documents/2016_cvrf.json

--csv file path
        Creates a CSV file in the specified path
        Example:
        >> openVulnQuery --config PathToCredentialsFile --cvrf --year 2016 --csv  /Users/bkorabik/Documents/2016_cvrf.csv
```
#### Count (Optional)
Returns the count of fields entered with -f or --fields. If no fields are entered the base API fields are counted and displayed
```
-c

        Examples:
        >> openVulnQuery --config PathToCredentialsFile --cvrf --year 2016 -c
        >> # export CLIENT_ID and CLIENT_SECRET or write to config.py ... then:
        >> openVulnQuery --cvrf --severity low -f sir cves bug_ids -c
```

#### Developers
- Update the config.py file with client id and secret
- Directly interact with query_client.py to query the Open Vuln API
- query_client.py returns Advisory Object
- advisory.py module has Advisory object a abstract class which is inherited by CVRF and OVAL data type
- This abstraction hides the implementation details and the data source used to populate the data type. The data members of CVRF and OVAL advisories are populated from API results.

#### Disclosures:
No support for filtering based on --API fields, you can't use --year 2016 and --severity high

Filtering with Grep:
```
Finding the Number of CVRF Advisories with a "Critical" sir in 2013
        >> openVulnQuery --config PathToCredentialsFile --cvrf --year 2013 -f sir | grep -c "Critical"
        >> openVulnQuery --config PathToCredentialsFile --cvrf --severity critical -f first_published | grep -c "2013"
```

If more than one API filter is entered, the last filter will be used for the API call.

You can alternatively use the date range functionality, as shown below:

```
>> openVulnQuery --config PathToCredentialsFile --cvrf --severity critical --first_published 2017-01-02:2017-10-01
```

#### Run OpenVulnQuery as a Library
After you install openVulnQuery package, you can use the query_client module to make API-call which returns
 advisory objects. For each query to the API, you can pick the advisory format.
```
>> from openVulnQuery import query_client
>> query_client = query_client.OpenVulnQueryClient(client_id="", client_secret="")
>> advisories = query_client.get_by_year(year=2010, adv_format='cvrf')
>> advisories = query_client.get_by_ios_xe('ios', '3.16.1S')
```
If you want to use the additional date filters based on first published and last updated date. You can pass the appropriate class
```
>> advisories = query_client.get_by_severity(adv_format='cvrf', severity='high', FirstPublished(2016-01-01, 2016-02-02))
>> advisories = query_client.get_by_severity(adv_format='oval', severity='low', LastUpdated(2016-01-01, 2016-02-02))
```

##### Debugging Requests and Responses

If the run time environment has the variable `CISCO_OPEN_VULN_API_DEBUG` 
set (and the value evaluates to True) the data forming every request as well 
as raw and formatted variants of successful responses (`HTTP 200/OK`)
will be written to files in JSON format.

The file names follow the pattern: `ts-{ts}_id-{id}_snapshot-of-{kind}.json`, 
where: 

* `{ts}` receives a date time stamp as ruled by the module variable 
`DEBUG_TIME_STAMP_FORMAT` (default `%Y%m%dT%H%M%S.%f`) and noted in local
time,
* `{id}` is a string holding a UUID4 generated for the request and useful to
 correlate request and response data files
* `{kind}` is one of three strings speaking for themselves: 
  + `request`
  + `response-raw`
  + `response-formated`

The files will be written either to the current folder, or to a path stored
in the environment variable `CISCO_OPEN_VULN_API_PATH` (if it is set).

*Note*: The folder at that later path is expected to exist and be writeable 
by the user. Please note also, that Filesystem and JSON serialization errors
are ignored.

Here are the information stored in advisory object.
##### Advisory
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

##### CVRF (inherits Advisory Abstract Class)
            * cvrf_url
            * vuln_title
##### OVAL (inherits Advisory Abstract Class)
            * oval_url
After you install openVulnQuery package, you can use the query_client module to make API-call which returns
 advisory objects. For each query to the API, you can pick advisory format.
```
>> from openVulnQuery import query_client
>> query_client = query_client.OpenVulnQueryClient(client_id='', client_secret='')
>> advisories = query_client.get_by_year(year=2010, adv_format='cvrf')
```
Here are the information stored in advisory object.
##### Advisory (Abstract Base Class)
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
##### CVRF
        * cvrf_url
##### OVAL
        * oval_url
##### AdvisoryIOS
        * ios_release
        * first_fixed
        * cvrf_url
        * oval_url


### Running the tests

To run the tests in the tests folder, the additional required `mock` module should be installed inside the `venv`with the usual:

```
pip install mock pytest
```

There are unit tests in `tests/` and some sample like system level test (`tests/test_query_client_cvrf.py`) skipped in below sample runs, as it contacting the real API.

Sample run (expecting `pytest` has been installed e.g. via `pip install pytest`):

```
$ cd /www/github.com/CiscoPSIRT/openVulnAPI/openVulnQuery

$ pytest
=========================================================================================================== test session starts ============================================================================================================
platform darwin -- Python 2.7.13, pytest-3.1.2, py-1.4.34, pluggy-0.4.0
rootdir: /www/github.com/CiscoPSIRT/openVulnAPI/openVulnQuery, inifile:
plugins: cov-2.5.1
collected 159 items 

tests/test_advisory.py ......................
tests/test_authorization.py ...
tests/test_cli_api.py ..............................................
tests/test_config.py ....
tests/test_constants.py ...........
tests/test_main.py ...........................s......
tests/test_query_client.py ................
tests/test_query_client_cvrf.py ssssssss
tests/test_utils.py ...............

================================================================================================== 150 passed, 9 skipped in 1.16 seconds ===================================================================================================
```

Including coverage info (requires `pip install pytest-cov` which includes `pip install coverage` ):

```
$ pytest --cov=openVulnQuery --cov-report=term-missing --cov-report=html
=========================================================================================================== test session starts ============================================================================================================
platform darwin -- Python 2.7.13, pytest-3.1.2, py-1.4.34, pluggy-0.4.0
rootdir: /www/github.com/CiscoPSIRT/openVulnAPI/openVulnQuery, inifile:
plugins: cov-2.5.1
collected 159 items 

tests/test_advisory.py ......................
tests/test_authorization.py ...
tests/test_cli_api.py ..............................................
tests/test_config.py ....
tests/test_constants.py ...........
tests/test_main.py ...........................s......
tests/test_query_client.py ................
tests/test_query_client_cvrf.py ssssssss
tests/test_utils.py ...............

---------- coverage: platform darwin, python 2.7.13-final-0 ----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
openVulnQuery/__init__.py            0      0   100%
openVulnQuery/advisory.py           90      1    99%   59
openVulnQuery/authorization.py       6      0   100%
openVulnQuery/cli_api.py            75      4    95%   294-297, 311
openVulnQuery/config.py              4      0   100%
openVulnQuery/constants.py          11      0   100%
openVulnQuery/main.py               38      6    84%   57, 60-65, 70
openVulnQuery/query_client.py      100     16    84%   128-134, 148-155, 160-167
openVulnQuery/rest_api.py            3      0   100%
openVulnQuery/utils.py              76     12    84%   109, 118-129
--------------------------------------------------------------
TOTAL                              403     39    90%
Coverage HTML written to dir htmlcov


================================================================================================== 150 passed, 9 skipped in 1.60 seconds ===================================================================================================
```
