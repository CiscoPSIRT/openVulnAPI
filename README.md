# Cisco PSIRT openVuln API

## Overview
The Cisco PSIRT openVuln API is a RESTful API that allows customers to obtain Cisco security vulnerability information in different machine-consumable formats. It supports industrywide security standards such as the OASIS Common Security Advisory Framework (CSAF) Common Vulnerability Reporting Framework (CVRF), Common Vulnerability and Exposure (CVE) identifiers, Common Weakness Enumerator (CWE), and the Common Vulnerability Scoring System (CVSS).

This API allows technical staff and programmers to build tools that help them do their job more effectively. In this case, it enables them to easily keep up with security vulnerability information specific to their network. That frees up more time for them to manage their network and deploy new capabilities in their infrastructure.

The API also allows Cisco customers and partners to leverage machine readable data to keep-up with Cisco security advisories. It further simplifies the evaluation process and reduces the time between when a vulnerability is announced and the fix is actually implemented. T

For more information about the openVuln API and how to access it visit:
https://developer.cisco.com/site/PSIRT/

---

## API Methods
The following are the methods supported by the openVuln API:
The base URL of the API is: https://api.cisco.com/security/advisories

### Querying by Advisory ID
|Method | `GET /security/advisories/advisory/{advisory_id}`|
|---|---|
| Description | Used to obtain an advisory given its advisory ID advisory_id (e.g., `cisco-sa-20180221-ucdm`) |

Example:

`curl -X GET "https://api.cisco.com/security/advisories/advisory/{advisory_id}"`

#### Responses
Status: 200 - Successful response

#### Error Codes

Scenario: The following error will be returned if the `advisory_id` is not found.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>ADVISORYID_NOT_FOUND</errorCode>
  <errorMessage>Advisory-id not found</errorMessage>
</advisory>
```

Scenario: The following error will be returned if the extension entered is not a valid extension

**Note**: This applies to all resource URIs.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>INVALID_EXTENSION</errorCode>
  <errorMessage>Not supported extension type. Supported extension types are .json and .xml</errorMessage>
</advisory>
```

---

### Obtaining All Advisories

|Method | `GET /security/advisories/all` |
|---|---|
| Description:| Used to obtain information about all published security advisories. <br> By default the output is in JSON. To obtain the output in XML use the .xml extension (e.g., `/advisories/all.xml`) |

Example:

`curl -X GET "https://api.cisco.com/security/advisories/all"`

You can query advisories using a "first published" date range, as shown below:

`https://api.cisco.com/security/advisories/all/firstpublished?startDate=2018-01-01&endDate=2018-02-15`

The same concept applies when querying advisories that have a given security impact rating:

`https://api.cisco.com/security/advisories/severity/critical/lastpublished?startDate=2017-01-01&endDate=2017-02-15`
`https://api.cisco.com/security/advisories/severity/high/firstpublished?startDate=2017-01-01&endDate=2017-02-15`

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario:	The following error will be returned if the page index is not a valid index

**Note**: This applies to all resource URIs.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>INVALID_PAGEINDEX</errorCode>
  <errorMessage>Incorrect page index value</errorMessage>
</advisory>

```
Scenario:	The following error will be returned if the page size is not a valid

**Note**: This applies to all resource URIs.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>MIN_PAGESIZE , MAX_PAGESIZE</errorCode>
  <errorMessage>Incorrect page size. Minimum page size value = 1 and Maximum page size = 100</errorMessage>
</advisory>
```

---

### Querying by CVE ID
|Method | `GET /security/advisories/cve/{cve_id}`|
|---|---|
| Description | Used to obtain an advisory using a given Common Vulnerability Enumerator (CVE). The `cve_id` format is CVE-YYYY-NNNN. <br>
For more information about CVE visit http://cve.mitre.org/ |

Example:

`curl -X GET "https://api.cisco.com/security/advisories/cve/{cve_id}"`

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario: The following error will be returned if the `cve_id` is not found in the database.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>NO_DATA_FOUND</errorCode>
  <errorMessage>CVE_ID not found</errorMessage>
</advisory>
```

---

### Querying the Latest Advisories
|Method | `GET /security/advisories/latest/{number}`|
|---|---|
| Description | Using an absolute number to obtain the latest security advisories.|

Example:

`curl -X GET "https://api.cisco.com/security/advisories/latest/5"`

This will return the latest 5 security advisories.

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario: The following error will be returned if the `latest` count is invalid. The `latest` count should be between 1 and 100.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>MIN_ADV_COUNT,MAX_ADV_COUNT</errorCode>
  <errorMessage>Minimum latest advisories count is 1,Maximum latest advisories count is 100</errorMessage>
</advisory>
```

---

### Querying by the Product Name
|Method | `GET /security/advisories/product/{product_keyword}`|
|---|---|
| Description | Used to obtain all the advisories that affects the given product name.|

Example:

`curl -X GET "https://api.cisco.com/security/advisories/product?product="`

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario: The following error will be returned if the product name is not found:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>NO_DATA_FOUND</errorCode>
  <errorMessage>No data found</errorMessage>
</advisory>
```
---

### Querying by the Security Impact Rating (SIR)
|Method | `GET /security/advisories/severity/{severity}/firstpublished`|
|---|---|
| Description | Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) and additionally filter based of `firstpublished` start and end date.|

Example:

`curl -X GET "https://api.cisco.com/security/advisories/severity/{severity}/firstpublished?startDate=&endDate="`

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario: The following error will be returned if no advisories by a given severity are found:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>NO_DATA_FOUND</errorCode>
  <errorMessage>No data found</errorMessage>
</advisory>
```

---

### Querying by the Year the Advisory was Published
|Method | `GET /security/advisories/year/{year}`|
|---|---|
| Description | Used to obtain all security advisories published in a given year. |

Example:

`curl -X GET "https://api.cisco.com/security/advisories/year/{year}"`

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario: The following error will be returned if the year is incorrect. The `year` must be between 1995 and current year.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>INVALID_YEAR</errorCode>
  <errorMessage>Year should be in range 1995 to current year</errorMessage>
</advisory>
```

Scenario: The following error will be returned if no advisories are found for a given year.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>NO_DATA_FOUND</errorCode>
  <errorMessage>No data found</errorMessage>
</advisory>
```

---

### Querying by a Given Cisco IOS Software Version
|Method | `GET /security/advisories/ios`|
|---|---|
| Description | This functionality allows you to query the [Cisco IOS Software Checker](https://tools.cisco.com/security/center/softwarechecker.x). <br> This method is used to obtain Cisco Security Advisories that apply to specific Cisco IOS Software releases and have a Security Impact Rating (SIR) of Critical or High.|

Example:

`curl -X GET "https://api.cisco.com/security/advisories/ios?version="`

#### Responses
Status: 200 - Successful response

#### Error Codes
Scenario: The following error will be returned if no advisories are found for a given Cisco IOS Software version.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>NO_DATA_FOUND</errorCode>
  <errorMessage>No data found</errorMessage>
</advisory>
```

---

### Querying by a Given Cisco IOS-XE Software Version
|Method | `GET /security/advisories/iosxe`|
|---|---|
| Description | This functionality allows you to query the [Cisco IOS Software Checker](https://tools.cisco.com/security/center/softwarechecker.x). <br> This method is used to obtain Cisco Security Advisories that apply to specific Cisco IOS-XE Software releases and have a Security Impact Rating (SIR) of Critical or High.|

Example:

`curl -X GET "https://api.cisco.com/security/advisories/iosxe?version="`

#### Responses
Status: 200 - Successful response


#### Error Codes
Scenario: The following error will be returned if no advisories are found for a given Cisco IOS-XE Software version.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<advisory>
  <errorCode>NO_DATA_FOUND</errorCode>
  <errorMessage>No data found</errorMessage>
</advisory>
```

---

### Pagination
The Cisco PSIRT openVuln API supports pagination using the page index and page size parameters, as demonstrated below:

`https://api.cisco.com/security/advisories/severity/critical?pageIndex=1&pageSize=100`

The pageIndex field is an integer representing the current page index out of total number of pages (TNP).
```
  Total advisories / pageSize = TNP
  (1000 / 100 = 10)
```
The pageSize field is an integer representing the maximum number of items requested by the client for the current page. The maximum pageSize limit is 100.

The following resource URIs support pagination.
```  
    /advisories/severity/critical?pageIndex=1&pageSize=100
    /advisories/severity/high?pageIndex=1&pageSize=100
    /advisories/severity/medium?pageIndex=1&pageSize=100
    /advisories/severity/low?pageIndex=1&pageSize=100
    /advisories/all?pageIndex=1&pageSize=100
    /advisories/year/YYYY?pageIndex=1&pageSize=100
```
