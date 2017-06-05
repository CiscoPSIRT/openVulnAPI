# \DefaultApi

All URIs are relative to *https://api.cisco.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SecurityAdvisoriesCvrfAdvisoryAdvisoryIdGet**](DefaultApi.md#SecurityAdvisoriesCvrfAdvisoryAdvisoryIdGet) | **Get** /security/advisories/cvrf/advisory/{advisory_id} | 
[**SecurityAdvisoriesCvrfAllGet**](DefaultApi.md#SecurityAdvisoriesCvrfAllGet) | **Get** /security/advisories/cvrf/all | 
[**SecurityAdvisoriesCvrfCveCveIdGet**](DefaultApi.md#SecurityAdvisoriesCvrfCveCveIdGet) | **Get** /security/advisories/cvrf/cve/{cve_id} | 
[**SecurityAdvisoriesCvrfLatestNumberGet**](DefaultApi.md#SecurityAdvisoriesCvrfLatestNumberGet) | **Get** /security/advisories/cvrf/latest/{number} | 
[**SecurityAdvisoriesCvrfProductGet**](DefaultApi.md#SecurityAdvisoriesCvrfProductGet) | **Get** /security/advisories/cvrf/product | 
[**SecurityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**](DefaultApi.md#SecurityAdvisoriesCvrfSeveritySeverityFirstpublishedGet) | **Get** /security/advisories/cvrf/severity/{severity}/firstpublished | 
[**SecurityAdvisoriesCvrfSeveritySeverityGet**](DefaultApi.md#SecurityAdvisoriesCvrfSeveritySeverityGet) | **Get** /security/advisories/cvrf/severity/{severity} | 
[**SecurityAdvisoriesCvrfSeveritySeverityLastpublishedGet**](DefaultApi.md#SecurityAdvisoriesCvrfSeveritySeverityLastpublishedGet) | **Get** /security/advisories/cvrf/severity/{severity}/lastpublished | 
[**SecurityAdvisoriesCvrfYearYearGet**](DefaultApi.md#SecurityAdvisoriesCvrfYearYearGet) | **Get** /security/advisories/cvrf/year/{year} | 
[**SecurityAdvisoriesIosGet**](DefaultApi.md#SecurityAdvisoriesIosGet) | **Get** /security/advisories/ios | 
[**SecurityAdvisoriesIosxeGet**](DefaultApi.md#SecurityAdvisoriesIosxeGet) | **Get** /security/advisories/iosxe | 
[**SecurityAdvisoriesOvalAdvisoryAdvisoryIdGet**](DefaultApi.md#SecurityAdvisoriesOvalAdvisoryAdvisoryIdGet) | **Get** /security/advisories/oval/advisory/{advisory_id} | 
[**SecurityAdvisoriesOvalAllGet**](DefaultApi.md#SecurityAdvisoriesOvalAllGet) | **Get** /security/advisories/oval/all | 
[**SecurityAdvisoriesOvalCveCveIdGet**](DefaultApi.md#SecurityAdvisoriesOvalCveCveIdGet) | **Get** /security/advisories/oval/cve/{cve_id} | 
[**SecurityAdvisoriesOvalLatestNumberGet**](DefaultApi.md#SecurityAdvisoriesOvalLatestNumberGet) | **Get** /security/advisories/oval/latest/{number} | 
[**SecurityAdvisoriesOvalProductGet**](DefaultApi.md#SecurityAdvisoriesOvalProductGet) | **Get** /security/advisories/oval/product | 
[**SecurityAdvisoriesOvalSeveritySeverityFirstpublishedGet**](DefaultApi.md#SecurityAdvisoriesOvalSeveritySeverityFirstpublishedGet) | **Get** /security/advisories/oval/severity/{severity}/firstpublished | 
[**SecurityAdvisoriesOvalSeveritySeverityGet**](DefaultApi.md#SecurityAdvisoriesOvalSeveritySeverityGet) | **Get** /security/advisories/oval/severity/{severity} | 
[**SecurityAdvisoriesOvalSeveritySeverityLastpublishedGet**](DefaultApi.md#SecurityAdvisoriesOvalSeveritySeverityLastpublishedGet) | **Get** /security/advisories/oval/severity/{severity}/lastpublished | 


# **SecurityAdvisoriesCvrfAdvisoryAdvisoryIdGet**
> SecurityAdvisoriesCvrfAdvisoryAdvisoryIdGet($advisoryId)



Used to obtain an advisory in CVRF format for a given advisory ID `advisory_id` (i.e., cisco-sa-20150819-pcp) 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisoryId** | **string**| advisory ID | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfAllGet**
> SecurityAdvisoriesCvrfAllGet()



Used to obtain all advisories in Common Vulnerability Reporting Format (CVRF). For more information about CVRF go to https://communities.cisco.com/docs/DOC-63156 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/cvrf/all.xml 


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfCveCveIdGet**
> SecurityAdvisoriesCvrfCveCveIdGet($cveId)



Used to obtain an advisory in CVRF format for a given Common Vulnerability Enumerator (CVE). The `cve_id` format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cveId** | **string**| CVE Identifier (i.e., CVE-YYYY-NNNN) | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfLatestNumberGet**
> SecurityAdvisoriesCvrfLatestNumberGet($number)



Used to obtain all the latest security advisories in CVRF format given an absolute number. For instance, the latest 10 or latest 5. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int32**| An absolute number to obtain the latest security advisories. | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfProductGet**
> SecurityAdvisoriesCvrfProductGet($product)



Used to obtain all the advisories that affects the given product name. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **string**| An product name to obtain security advisories that matches given product name. | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**
> SecurityAdvisoriesCvrfSeveritySeverityFirstpublishedGet($severity, $startDate, $endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format and additionally filter based of firstpublished start date and enddate 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **string**| Used to obtain all advisories that have a security impact rating of critical | 
 **startDate** | **time.Time**|  | 
 **endDate** | **time.Time**|  | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfSeveritySeverityGet**
> SecurityAdvisoriesCvrfSeveritySeverityGet($severity)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **string**| Critical, High, Medium, Low | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfSeveritySeverityLastpublishedGet**
> SecurityAdvisoriesCvrfSeveritySeverityLastpublishedGet($severity, $startDate, $endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **string**| Used to obtain all advisories that have a security impact rating of critical | 
 **startDate** | **time.Time**|  | 
 **endDate** | **time.Time**|  | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesCvrfYearYearGet**
> SecurityAdvisoriesCvrfYearYearGet($year)



Used to obtain all security advisories that have were orginally published in a specific year `YYYY`. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **string**| The four digit year. | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesIosGet**
> SecurityAdvisoriesIosGet($version)



Used to obtain all advisories that affects the given ios version 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **string**| IOS version to obtain security advisories | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesIosxeGet**
> SecurityAdvisoriesIosxeGet($version)



Used to obtain all advisories that affects the given ios version 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **string**| IOS version to obtain security advisories | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalAdvisoryAdvisoryIdGet**
> SecurityAdvisoriesOvalAdvisoryAdvisoryIdGet($advisoryId)



Used to obtain OVAL definitions for a given advisory ID `advisory_id` (i.e., cisco-sa-20150819-pcp) 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisoryId** | **string**| advisory ID | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalAllGet**
> SecurityAdvisoriesOvalAllGet()



Used to obtain all Open Vulnerability and Assessment Language (OVAL) definitions available for Cisco security vulnerabilities. For more information about OVAL go to https://communities.cisco.com/docs/DOC-63158 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/oval/all.xml 


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalCveCveIdGet**
> SecurityAdvisoriesOvalCveCveIdGet($cveId)



Used to obtain OVAL definitions for a given CVE Identifier. The `cve_id` format is CVE-YYYY-NNNN. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cveId** | **string**| CVE Identifier (i.e., CVE-YYYY-NNNN) | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalLatestNumberGet**
> SecurityAdvisoriesOvalLatestNumberGet($number)



Used to obtain all the latest OVAL definitions given an absolute number. For instance, the latest 10 or latest 5. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int32**| The latest OVAL definitions (absolute number). | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalProductGet**
> SecurityAdvisoriesOvalProductGet($product)



Used to obtain all the oval advisories that affects the given product name. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **string**| An product name to obtain security advisories that matches given product name. | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalSeveritySeverityFirstpublishedGet**
> SecurityAdvisoriesOvalSeveritySeverityFirstpublishedGet($severity, $startDate, $endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **string**| Critical, High, Medium, Low | 
 **startDate** | **time.Time**|  | 
 **endDate** | **time.Time**|  | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalSeveritySeverityGet**
> SecurityAdvisoriesOvalSeveritySeverityGet($severity)



Used to obtain all OVAL definitions for a given security impact rating (critical, high, medium, or low). 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **string**| Used to obtain all OVAL definitions for advisories that have a security impact rating of critical | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SecurityAdvisoriesOvalSeveritySeverityLastpublishedGet**
> SecurityAdvisoriesOvalSeveritySeverityLastpublishedGet($severity, $startDate, $endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **string**| Critical, High, Medium, Low | 
 **startDate** | **time.Time**|  | 
 **endDate** | **time.Time**|  | 

### Return type

void (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

