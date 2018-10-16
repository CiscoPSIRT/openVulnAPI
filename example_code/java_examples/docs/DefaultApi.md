# DefaultApi

All URIs are relative to *https://api.cisco.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityAdvisoriesAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesAdvisoryAdvisoryIdGet) | **GET** /security/advisories/advisory/{advisory_id} | 
[**securityAdvisoriesAllGet**](DefaultApi.md#securityAdvisoriesAllGet) | **GET** /security/advisories/all | 
[**securityAdvisoriesCveCveIdGet**](DefaultApi.md#securityAdvisoriesCveCveIdGet) | **GET** /security/advisories/cve/{cve_id} | 
[**securityAdvisoriesIosGet**](DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios | 
[**securityAdvisoriesIosxeGet**](DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe | 
[**securityAdvisoriesLatestNumberGet**](DefaultApi.md#securityAdvisoriesLatestNumberGet) | **GET** /security/advisories/latest/{number} | 
[**securityAdvisoriesProductGet**](DefaultApi.md#securityAdvisoriesProductGet) | **GET** /security/advisories/product | 
[**securityAdvisoriesSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/severity/{severity}/firstpublished | 
[**securityAdvisoriesSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesSeveritySeverityGet) | **GET** /security/advisories/severity/{severity} | 
[**securityAdvisoriesSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesSeveritySeverityLastpublishedGet) | **GET** /security/advisories/severity/{severity}/lastpublished | 
[**securityAdvisoriesYearYearGet**](DefaultApi.md#securityAdvisoriesYearYearGet) | **GET** /security/advisories/year/{year} | 


<a name="securityAdvisoriesAdvisoryAdvisoryIdGet"></a>
# **securityAdvisoriesAdvisoryAdvisoryIdGet**
> securityAdvisoriesAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain an advisory given its advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20180221-ucdm) 

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
    apiInstance.securityAdvisoriesAdvisoryAdvisoryIdGet(advisoryId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesAdvisoryAdvisoryIdGet");
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

<a name="securityAdvisoriesAllGet"></a>
# **securityAdvisoriesAllGet**
> securityAdvisoriesAllGet()



Used to obtain information about all published security advisories. By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/all.xml 

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
    apiInstance.securityAdvisoriesAllGet();
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesAllGet");
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

<a name="securityAdvisoriesCveCveIdGet"></a>
# **securityAdvisoriesCveCveIdGet**
> securityAdvisoriesCveCveIdGet(cveId)



Used to obtain an advisory using a given Common Vulnerability Enumerator (CVE). The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 

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
    apiInstance.securityAdvisoriesCveCveIdGet(cveId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesCveCveIdGet");
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

<a name="securityAdvisoriesLatestNumberGet"></a>
# **securityAdvisoriesLatestNumberGet**
> securityAdvisoriesLatestNumberGet(number)



Used to obtain all the latest security advisories given an absolute number. For instance, the latest 10 or latest 5. 

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
    apiInstance.securityAdvisoriesLatestNumberGet(number);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesLatestNumberGet");
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

<a name="securityAdvisoriesProductGet"></a>
# **securityAdvisoriesProductGet**
> securityAdvisoriesProductGet(product)



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
    apiInstance.securityAdvisoriesProductGet(product);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesProductGet");
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

<a name="securityAdvisoriesSeveritySeverityFirstpublishedGet"></a>
# **securityAdvisoriesSeveritySeverityFirstpublishedGet**
> securityAdvisoriesSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) and additionally filter based of firstpublished start date and enddate. 

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
    apiInstance.securityAdvisoriesSeveritySeverityFirstpublishedGet(severity, startDate, endDate);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesSeveritySeverityFirstpublishedGet");
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

<a name="securityAdvisoriesSeveritySeverityGet"></a>
# **securityAdvisoriesSeveritySeverityGet**
> securityAdvisoriesSeveritySeverityGet(severity)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low). 

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
    apiInstance.securityAdvisoriesSeveritySeverityGet(severity);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesSeveritySeverityGet");
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

<a name="securityAdvisoriesSeveritySeverityLastpublishedGet"></a>
# **securityAdvisoriesSeveritySeverityLastpublishedGet**
> securityAdvisoriesSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low). 

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
    apiInstance.securityAdvisoriesSeveritySeverityLastpublishedGet(severity, startDate, endDate);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesSeveritySeverityLastpublishedGet");
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

<a name="securityAdvisoriesYearYearGet"></a>
# **securityAdvisoriesYearYearGet**
> securityAdvisoriesYearYearGet(year)



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
    apiInstance.securityAdvisoriesYearYearGet(year);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#securityAdvisoriesYearYearGet");
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

