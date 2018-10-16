# \DefaultApi

All URIs are relative to *https://api.cisco.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SecurityAdvisoriesAdvisoryAdvisoryIdGet**](DefaultApi.md#SecurityAdvisoriesAdvisoryAdvisoryIdGet) | **Get** /security/advisories/advisory/{advisory_id} | 
[**SecurityAdvisoriesAllGet**](DefaultApi.md#SecurityAdvisoriesAllGet) | **Get** /security/advisories/all | 
[**SecurityAdvisoriesCveCveIdGet**](DefaultApi.md#SecurityAdvisoriesCveCveIdGet) | **Get** /security/advisories/cve/{cve_id} | 
[**SecurityAdvisoriesIosGet**](DefaultApi.md#SecurityAdvisoriesIosGet) | **Get** /security/advisories/ios | 
[**SecurityAdvisoriesIosxeGet**](DefaultApi.md#SecurityAdvisoriesIosxeGet) | **Get** /security/advisories/iosxe | 
[**SecurityAdvisoriesLatestNumberGet**](DefaultApi.md#SecurityAdvisoriesLatestNumberGet) | **Get** /security/advisories/latest/{number} | 
[**SecurityAdvisoriesProductGet**](DefaultApi.md#SecurityAdvisoriesProductGet) | **Get** /security/advisories/product | 
[**SecurityAdvisoriesSeveritySeverityFirstpublishedGet**](DefaultApi.md#SecurityAdvisoriesSeveritySeverityFirstpublishedGet) | **Get** /security/advisories/severity/{severity}/firstpublished | 
[**SecurityAdvisoriesSeveritySeverityGet**](DefaultApi.md#SecurityAdvisoriesSeveritySeverityGet) | **Get** /security/advisories/severity/{severity} | 
[**SecurityAdvisoriesSeveritySeverityLastpublishedGet**](DefaultApi.md#SecurityAdvisoriesSeveritySeverityLastpublishedGet) | **Get** /security/advisories/severity/{severity}/lastpublished | 
[**SecurityAdvisoriesYearYearGet**](DefaultApi.md#SecurityAdvisoriesYearYearGet) | **Get** /security/advisories/year/{year} | 


# **SecurityAdvisoriesAdvisoryAdvisoryIdGet**
> SecurityAdvisoriesAdvisoryAdvisoryIdGet(ctx, advisoryId)


Used to obtain an advisory given its advisory ID `advisory_id` (i.e., cisco-sa-20180221-ucdm) 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **advisoryId** | **string**| advisory ID | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesAllGet**
> SecurityAdvisoriesAllGet(ctx, )


Used to obtain information about all published security advisories. By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/all.xml 

### Required Parameters
This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCveCveIdGet**
> SecurityAdvisoriesCveCveIdGet(ctx, cveId)


Used to obtain an advisory using a given Common Vulnerability Enumerator (CVE). The `cve_id` format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **cveId** | **string**| CVE Identifier (i.e., CVE-YYYY-NNNN) | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesIosGet**
> SecurityAdvisoriesIosGet(ctx, version)


Used to obtain all advisories that affects the given ios version 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **version** | **string**| IOS version to obtain security advisories | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesIosxeGet**
> SecurityAdvisoriesIosxeGet(ctx, version)


Used to obtain all advisories that affects the given ios version 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **version** | **string**| IOS version to obtain security advisories | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesLatestNumberGet**
> SecurityAdvisoriesLatestNumberGet(ctx, number)


Used to obtain all the latest security advisories given an absolute number. For instance, the latest 10 or latest 5. 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **number** | **int32**| An absolute number to obtain the latest security advisories. | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesProductGet**
> SecurityAdvisoriesProductGet(ctx, product)


Used to obtain all the advisories that affects the given product name. 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **product** | **string**| An product name to obtain security advisories that matches given product name. | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesSeveritySeverityFirstpublishedGet**
> SecurityAdvisoriesSeveritySeverityFirstpublishedGet(ctx, severity, startDate, endDate)


Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) and additionally filter based of firstpublished start date and enddate. 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **severity** | **string**| Used to obtain all advisories that have a security impact rating of critical | 
  **startDate** | **string**|  | 
  **endDate** | **string**|  | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesSeveritySeverityGet**
> SecurityAdvisoriesSeveritySeverityGet(ctx, severity)


Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low). 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **severity** | **string**| Critical, High, Medium, Low | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesSeveritySeverityLastpublishedGet**
> SecurityAdvisoriesSeveritySeverityLastpublishedGet(ctx, severity, startDate, endDate)


Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low). 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **severity** | **string**| Used to obtain all advisories that have a security impact rating of critical | 
  **startDate** | **string**|  | 
  **endDate** | **string**|  | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesYearYearGet**
> SecurityAdvisoriesYearYearGet(ctx, year)


Used to obtain all security advisories that have were orginally published in a specific year `YYYY`. 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **year** | **string**| The four digit year. | 

### Return type

 (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

