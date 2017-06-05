# DefaultApi

All URIs are relative to *https://api.cisco.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityAdvisoriesCvrfAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesCvrfAdvisoryAdvisoryIdGet) | **GET** /security/advisories/cvrf/advisory/{advisory_id} | 
[**securityAdvisoriesCvrfAllGet**](DefaultApi.md#securityAdvisoriesCvrfAllGet) | **GET** /security/advisories/cvrf/all | 
[**securityAdvisoriesCvrfCveCveIdGet**](DefaultApi.md#securityAdvisoriesCvrfCveCveIdGet) | **GET** /security/advisories/cvrf/cve/{cve_id} | 
[**securityAdvisoriesCvrfLatestNumberGet**](DefaultApi.md#securityAdvisoriesCvrfLatestNumberGet) | **GET** /security/advisories/cvrf/latest/{number} | 
[**securityAdvisoriesCvrfProductGet**](DefaultApi.md#securityAdvisoriesCvrfProductGet) | **GET** /security/advisories/cvrf/product | 
[**securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/firstpublished | 
[**securityAdvisoriesCvrfSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityGet) | **GET** /security/advisories/cvrf/severity/{severity} | 
[**securityAdvisoriesCvrfSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityLastpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/lastpublished | 
[**securityAdvisoriesCvrfYearYearGet**](DefaultApi.md#securityAdvisoriesCvrfYearYearGet) | **GET** /security/advisories/cvrf/year/{year} | 
[**securityAdvisoriesIosGet**](DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios | 
[**securityAdvisoriesIosxeGet**](DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe | 
[**securityAdvisoriesOvalAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesOvalAdvisoryAdvisoryIdGet) | **GET** /security/advisories/oval/advisory/{advisory_id} | 
[**securityAdvisoriesOvalAllGet**](DefaultApi.md#securityAdvisoriesOvalAllGet) | **GET** /security/advisories/oval/all | 
[**securityAdvisoriesOvalCveCveIdGet**](DefaultApi.md#securityAdvisoriesOvalCveCveIdGet) | **GET** /security/advisories/oval/cve/{cve_id} | 
[**securityAdvisoriesOvalLatestNumberGet**](DefaultApi.md#securityAdvisoriesOvalLatestNumberGet) | **GET** /security/advisories/oval/latest/{number} | 
[**securityAdvisoriesOvalProductGet**](DefaultApi.md#securityAdvisoriesOvalProductGet) | **GET** /security/advisories/oval/product | 
[**securityAdvisoriesOvalSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/firstpublished | 
[**securityAdvisoriesOvalSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityGet) | **GET** /security/advisories/oval/severity/{severity} | 
[**securityAdvisoriesOvalSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityLastpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/lastpublished | 


<a name="securityAdvisoriesCvrfAdvisoryAdvisoryIdGet"></a>
# **securityAdvisoriesCvrfAdvisoryAdvisoryIdGet**
> securityAdvisoriesCvrfAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain an advisory in CVRF format for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String advisoryId = "advisoryId_example"; // String | advisory ID
try {
    apiInstance.securityAdvisoriesCvrfAdvisoryAdvisoryIdGet(advisoryId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfAdvisoryAdvisoryIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisoryId** | **String**| advisory ID |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfAllGet"></a>
# **securityAdvisoriesCvrfAllGet**
> securityAdvisoriesCvrfAllGet()



Used to obtain all advisories in Common Vulnerability Reporting Format (CVRF). For more information about CVRF go to https://communities.cisco.com/docs/DOC-63156 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/cvrf/all.xml 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
try {
    apiInstance.securityAdvisoriesCvrfAllGet();
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfAllGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfCveCveIdGet"></a>
# **securityAdvisoriesCvrfCveCveIdGet**
> securityAdvisoriesCvrfCveCveIdGet(cveId)



Used to obtain an advisory in CVRF format for a given Common Vulnerability Enumerator (CVE). The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String cveId = "cveId_example"; // String | CVE Identifier (i.e., CVE-YYYY-NNNN)
try {
    apiInstance.securityAdvisoriesCvrfCveCveIdGet(cveId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfCveCveIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cveId** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfLatestNumberGet"></a>
# **securityAdvisoriesCvrfLatestNumberGet**
> securityAdvisoriesCvrfLatestNumberGet(number)



Used to obtain all the latest security advisories in CVRF format given an absolute number. For instance, the latest 10 or latest 5. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
Integer number = 56; // Integer | An absolute number to obtain the latest security advisories.
try {
    apiInstance.securityAdvisoriesCvrfLatestNumberGet(number);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfLatestNumberGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **Integer**| An absolute number to obtain the latest security advisories. |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfProductGet"></a>
# **securityAdvisoriesCvrfProductGet**
> securityAdvisoriesCvrfProductGet(product)



Used to obtain all the advisories that affects the given product name. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String product = "product_example"; // String | An product name to obtain security advisories that matches given product name.
try {
    apiInstance.securityAdvisoriesCvrfProductGet(product);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfProductGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **String**| An product name to obtain security advisories that matches given product name. |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet"></a>
# **securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**
> securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format and additionally filter based of firstpublished start date and enddate 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String severity = "severity_example"; // String | Used to obtain all advisories that have a security impact rating of critical
LocalDate startDate = new LocalDate(); // LocalDate | 
LocalDate endDate = new LocalDate(); // LocalDate | 
try {
    apiInstance.securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet(severity, startDate, endDate);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical | [enum: critical, high, medium, low]
 **startDate** | **LocalDate**|  |
 **endDate** | **LocalDate**|  |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfSeveritySeverityGet"></a>
# **securityAdvisoriesCvrfSeveritySeverityGet**
> securityAdvisoriesCvrfSeveritySeverityGet(severity)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String severity = "severity_example"; // String | Critical, High, Medium, Low
try {
    apiInstance.securityAdvisoriesCvrfSeveritySeverityGet(severity);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfSeveritySeverityGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Critical, High, Medium, Low | [enum: critical, high, medium, low]

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfSeveritySeverityLastpublishedGet"></a>
# **securityAdvisoriesCvrfSeveritySeverityLastpublishedGet**
> securityAdvisoriesCvrfSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String severity = "severity_example"; // String | Used to obtain all advisories that have a security impact rating of critical
LocalDate startDate = new LocalDate(); // LocalDate | 
LocalDate endDate = new LocalDate(); // LocalDate | 
try {
    apiInstance.securityAdvisoriesCvrfSeveritySeverityLastpublishedGet(severity, startDate, endDate);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfSeveritySeverityLastpublishedGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical | [enum: critical, high, medium, low]
 **startDate** | **LocalDate**|  |
 **endDate** | **LocalDate**|  |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesCvrfYearYearGet"></a>
# **securityAdvisoriesCvrfYearYearGet**
> securityAdvisoriesCvrfYearYearGet(year)



Used to obtain all security advisories that have were orginally published in a specific year &#x60;YYYY&#x60;. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String year = "year_example"; // String | The four digit year.
try {
    apiInstance.securityAdvisoriesCvrfYearYearGet(year);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfYearYearGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **String**| The four digit year. |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesIosGet"></a>
# **securityAdvisoriesIosGet**
> securityAdvisoriesIosGet(version)



Used to obtain all advisories that affects the given ios version 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String version = "version_example"; // String | IOS version to obtain security advisories
try {
    apiInstance.securityAdvisoriesIosGet(version);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesIosGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**| IOS version to obtain security advisories |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesIosxeGet"></a>
# **securityAdvisoriesIosxeGet**
> securityAdvisoriesIosxeGet(version)



Used to obtain all advisories that affects the given ios version 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String version = "version_example"; // String | IOS version to obtain security advisories
try {
    apiInstance.securityAdvisoriesIosxeGet(version);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesIosxeGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**| IOS version to obtain security advisories |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalAdvisoryAdvisoryIdGet"></a>
# **securityAdvisoriesOvalAdvisoryAdvisoryIdGet**
> securityAdvisoriesOvalAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain OVAL definitions for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String advisoryId = "advisoryId_example"; // String | advisory ID
try {
    apiInstance.securityAdvisoriesOvalAdvisoryAdvisoryIdGet(advisoryId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalAdvisoryAdvisoryIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisoryId** | **String**| advisory ID |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalAllGet"></a>
# **securityAdvisoriesOvalAllGet**
> securityAdvisoriesOvalAllGet()



Used to obtain all Open Vulnerability and Assessment Language (OVAL) definitions available for Cisco security vulnerabilities. For more information about OVAL go to https://communities.cisco.com/docs/DOC-63158 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/oval/all.xml 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
try {
    apiInstance.securityAdvisoriesOvalAllGet();
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalAllGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalCveCveIdGet"></a>
# **securityAdvisoriesOvalCveCveIdGet**
> securityAdvisoriesOvalCveCveIdGet(cveId)



Used to obtain OVAL definitions for a given CVE Identifier. The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String cveId = "cveId_example"; // String | CVE Identifier (i.e., CVE-YYYY-NNNN)
try {
    apiInstance.securityAdvisoriesOvalCveCveIdGet(cveId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalCveCveIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cveId** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalLatestNumberGet"></a>
# **securityAdvisoriesOvalLatestNumberGet**
> securityAdvisoriesOvalLatestNumberGet(number)



Used to obtain all the latest OVAL definitions given an absolute number. For instance, the latest 10 or latest 5. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
Integer number = 56; // Integer | The latest OVAL definitions (absolute number).
try {
    apiInstance.securityAdvisoriesOvalLatestNumberGet(number);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalLatestNumberGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **Integer**| The latest OVAL definitions (absolute number). |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalProductGet"></a>
# **securityAdvisoriesOvalProductGet**
> securityAdvisoriesOvalProductGet(product)



Used to obtain all the oval advisories that affects the given product name. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String product = "product_example"; // String | An product name to obtain security advisories that matches given product name.
try {
    apiInstance.securityAdvisoriesOvalProductGet(product);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalProductGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **String**| An product name to obtain security advisories that matches given product name. |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalSeveritySeverityFirstpublishedGet"></a>
# **securityAdvisoriesOvalSeveritySeverityFirstpublishedGet**
> securityAdvisoriesOvalSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String severity = "severity_example"; // String | Critical, High, Medium, Low
LocalDate startDate = new LocalDate(); // LocalDate | 
LocalDate endDate = new LocalDate(); // LocalDate | 
try {
    apiInstance.securityAdvisoriesOvalSeveritySeverityFirstpublishedGet(severity, startDate, endDate);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalSeveritySeverityFirstpublishedGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Critical, High, Medium, Low | [enum: critical, high, medium, low]
 **startDate** | **LocalDate**|  |
 **endDate** | **LocalDate**|  |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalSeveritySeverityGet"></a>
# **securityAdvisoriesOvalSeveritySeverityGet**
> securityAdvisoriesOvalSeveritySeverityGet(severity)



Used to obtain all OVAL definitions for a given security impact rating (critical, high, medium, or low). 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String severity = "severity_example"; // String | Used to obtain all OVAL definitions for advisories that have a security impact rating of critical
try {
    apiInstance.securityAdvisoriesOvalSeveritySeverityGet(severity);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalSeveritySeverityGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Used to obtain all OVAL definitions for advisories that have a security impact rating of critical | [enum: critical, high, medium, low]

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="securityAdvisoriesOvalSeveritySeverityLastpublishedGet"></a>
# **securityAdvisoriesOvalSeveritySeverityLastpublishedGet**
> securityAdvisoriesOvalSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

DefaultApi apiInstance = new DefaultApi();
String severity = "severity_example"; // String | Critical, High, Medium, Low
LocalDate startDate = new LocalDate(); // LocalDate | 
LocalDate endDate = new LocalDate(); // LocalDate | 
try {
    apiInstance.securityAdvisoriesOvalSeveritySeverityLastpublishedGet(severity, startDate, endDate);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalSeveritySeverityLastpublishedGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Critical, High, Medium, Low | [enum: critical, high, medium, low]
 **startDate** | **LocalDate**|  |
 **endDate** | **LocalDate**|  |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

