# Error Codes
----
**Resource URIs:** cvrf/advisory/{advisoryId} or /oval/advisory/{advisoryId}

**Scenario:** If advisoryId is not found 	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>ADVISORYID_NOT_FOUND</errorCode>
      <errorMessage>Advisory-id not found</errorMessage>
    </advisory>

----
**Resource URI:** all
	
Scenario: If the extension entered is not a valid extension

**Note:** This will be common for all resource URIs.
	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>INVALID_EXTENSION</errorCode>
      <errorMessage>Not supported extension type. Supported extension types are .json and .xml</errorMessage>
    </advisory>

----
**Resource URIs:** all

**Scenario:**	Page index is not a valid index

Note: This will be common for all resource URIs.
	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>INVALID_PAGEINDEX</errorCode>
      <errorMessage>Incorrect page index value</errorMessage>
    </advisory>

----
**Resource URIs:** all

**Scenario:**	Page size is not a valid

**Note:** This will be common for all resource URIs.
	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>MIN_PAGESIZE , MAX_PAGESIZE</errorCode>
      <errorMessage>Incorrect page size. Minimum page size value = 1 and Maximum page size = 100</errorMessage>
    </advisory>
    
----
**Resource URIs:** /cvrf/severity/{severity} or /oval/severity/{severity}

**Scenario:**	If the severity (security impact rating) is not found. 	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>NO_DATA_FOUND</errorCode>
      <errorMessage>No data found</errorMessage>
    </advisory>

----
**Resource URIs:** /cvrf/cve/{cveId} or /oval/cve/{cveId}

**Scenario:** If cve id is not found in database

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>NO_DATA_FOUND</errorCode>
      <errorMessage>CVE_ID not found</errorMessage>
    </advisory>

----
**Resource URIs:** /cvrf/year/{year} or /oval/year/{year}

**Scenario:**	Year must be between 1995 and current year 	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>INVALID_YEAR</errorCode>
      <errorMessage>Year should be in range 1995 to current year</errorMessage>
    </advisory>

If no advisory found for given year.
	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>NO_DATA_FOUND</errorCode>
      <errorMessage>No data found</errorMessage>
    </advisory>

----
**Resource URIs:** /cvrf/latest/{advCount} or /oval/latest/{advCount}

**Scenario:**	If latest count is invalid, it should be between 1 and 100 	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>MIN_ADV_COUNT,MAX_ADV_COUNT</errorCode>
      <errorMessage>Minimum latest advisories count is 1,Maximum latest advisories count is 100</errorMessage>
    </advisory>

**Scenario:** If latest count is invalid, it should be between 1 and 100
	

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <advisory>
      <errorCode>MIN_ADV_COUNT,MAX_ADV_COUNT</errorCode>
      <errorMessage>Minimum latest advisories count is 1,Maximum latest advisories count is 100</errorMessage>
    </advisory>
