# SwaggerClient::DefaultApi

All URIs are relative to *https://api.cisco.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_advisories_advisory_advisory_id_get**](DefaultApi.md#security_advisories_advisory_advisory_id_get) | **GET** /security/advisories/advisory/{advisory_id} |
[**security_advisories_all_get**](DefaultApi.md#security_advisories_all_get) | **GET** /security/advisories/all |
[**security_advisories_cve_cve_id_get**](DefaultApi.md#security_advisories_cve_cve_id_get) | **GET** /security/advisories/cve/{cve_id} |
[**security_advisories_ios_get**](DefaultApi.md#security_advisories_ios_get) | **GET** /security/advisories/ios |
[**security_advisories_iosxe_get**](DefaultApi.md#security_advisories_iosxe_get) | **GET** /security/advisories/iosxe |
[**security_advisories_latest_number_get**](DefaultApi.md#security_advisories_latest_number_get) | **GET** /security/advisories/latest/{number} |
[**security_advisories_product_get**](DefaultApi.md#security_advisories_product_get) | **GET** /security/advisories/product |
[**security_advisories_severity_severity_firstpublished_get**](DefaultApi.md#security_advisories_severity_severity_firstpublished_get) | **GET** /security/advisories/severity/{severity}/firstpublished |
[**security_advisories_severity_severity_get**](DefaultApi.md#security_advisories_severity_severity_get) | **GET** /security/advisories/severity/{severity} |
[**security_advisories_severity_severity_lastpublished_get**](DefaultApi.md#security_advisories_severity_severity_lastpublished_get) | **GET** /security/advisories/severity/{severity}/lastpublished |
[**security_advisories_year_year_get**](DefaultApi.md#security_advisories_year_year_get) | **GET** /security/advisories/year/{year} |


# **security_advisories_advisory_advisory_id_get**
> security_advisories_advisory_advisory_id_get(advisory_id)



Used to obtain an advisory given its advisory ID `advisory_id` (i.e., cisco-sa-20180221-ucdm)

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

advisory_id = "advisory_id_example" # String | advisory ID


begin
  api_instance.security_advisories_advisory_advisory_id_get(advisory_id)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_advisory_advisory_id_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisory_id** | **String**| advisory ID |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_all_get**
> security_advisories_all_get



Used to obtain information about all published security advisories. By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/all.xml

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

begin
  api_instance.security_advisories_all_get
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_all_get: #{e}"
end
```

### Parameters
This endpoint does not need any parameter.

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_cve_cve_id_get**
> security_advisories_cve_cve_id_get(cve_id)



Used to obtain an advisory using a given Common Vulnerability Enumerator (CVE). The `cve_id` format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

cve_id = "cve_id_example" # String | CVE Identifier (i.e., CVE-YYYY-NNNN)


begin
  api_instance.security_advisories_cve_cve_id_get(cve_id)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_cve_cve_id_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_ios_get**
> security_advisories_ios_get(version)



Used to obtain all advisories that affects the given ios version

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

version = "version_example" # String | IOS version to obtain security advisories


begin
  api_instance.security_advisories_ios_get(version)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_ios_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**| IOS version to obtain security advisories |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_iosxe_get**
> security_advisories_iosxe_get(version)



Used to obtain all advisories that affects the given ios version

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

version = "version_example" # String | IOS version to obtain security advisories


begin
  api_instance.security_advisories_iosxe_get(version)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_iosxe_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**| IOS version to obtain security advisories |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_latest_number_get**
> security_advisories_latest_number_get(number)



Used to obtain all the latest security advisories given an absolute number. For instance, the latest 10 or latest 5.

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

number = 56 # Integer | An absolute number to obtain the latest security advisories.


begin
  api_instance.security_advisories_latest_number_get(number)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_latest_number_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **Integer**| An absolute number to obtain the latest security advisories. |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_product_get**
> security_advisories_product_get(product)



Used to obtain all the advisories that affects the given product name.

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

product = "product_example" # String | An product name to obtain security advisories that matches given product name.


begin
  api_instance.security_advisories_product_get(product)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_product_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **String**| An product name to obtain security advisories that matches given product name. |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_severity_severity_firstpublished_get**
> security_advisories_severity_severity_firstpublished_get(severity, start_date, end_date)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) and additionally filter based of firstpublished start date and enddate.

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

severity = "severity_example" # String | Used to obtain all advisories that have a security impact rating of critical

start_date = Date.parse("2013-10-20") # Date |

end_date = Date.parse("2013-10-20") # Date |


begin
  api_instance.security_advisories_severity_severity_firstpublished_get(severity, start_date, end_date)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_severity_severity_firstpublished_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical |
 **start_date** | **Date**|  |
 **end_date** | **Date**|  |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_severity_severity_get**
> security_advisories_severity_severity_get(severity)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low).

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

severity = "severity_example" # String | Critical, High, Medium, Low


begin
  api_instance.security_advisories_severity_severity_get(severity)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_severity_severity_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Critical, High, Medium, Low |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_severity_severity_lastpublished_get**
> security_advisories_severity_severity_lastpublished_get(severity, start_date, end_date)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low).

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

severity = "severity_example" # String | Used to obtain all advisories that have a security impact rating of critical

start_date = Date.parse("2013-10-20") # Date |

end_date = Date.parse("2013-10-20") # Date |


begin
  api_instance.security_advisories_severity_severity_lastpublished_get(severity, start_date, end_date)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_severity_severity_lastpublished_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical |
 **start_date** | **Date**|  |
 **end_date** | **Date**|  |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **security_advisories_year_year_get**
> security_advisories_year_year_get(year)



Used to obtain all security advisories that have were orginally published in a specific year `YYYY`.

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
  # Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = SwaggerClient::DefaultApi.new

year = "year_example" # String | The four digit year.


begin
  api_instance.security_advisories_year_year_get(year)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DefaultApi->security_advisories_year_year_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **String**| The four digit year. |

### Return type

nil (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json
