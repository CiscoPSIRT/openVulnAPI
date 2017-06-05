# swagger-java-client

## Requirements

Building the API client library requires [Maven](https://maven.apache.org/) to be installed.

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn deploy
```

Refer to the [official documentation](https://maven.apache.org/plugins/maven-deploy-plugin/usage.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-java-client</artifactId>
    <version>1.0.0</version>
    <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

    mvn package

Then manually install the following JARs:

* target/swagger-java-client-1.0.0.jar
* target/lib/*.jar

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.DefaultApi;

import java.io.File;
import java.util.*;

public class DefaultApiExample {

    public static void main(String[] args) {
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
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cisco.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**securityAdvisoriesCvrfAdvisoryAdvisoryIdGet**](docs/DefaultApi.md#securityAdvisoriesCvrfAdvisoryAdvisoryIdGet) | **GET** /security/advisories/cvrf/advisory/{advisory_id} | 
*DefaultApi* | [**securityAdvisoriesCvrfAllGet**](docs/DefaultApi.md#securityAdvisoriesCvrfAllGet) | **GET** /security/advisories/cvrf/all | 
*DefaultApi* | [**securityAdvisoriesCvrfCveCveIdGet**](docs/DefaultApi.md#securityAdvisoriesCvrfCveCveIdGet) | **GET** /security/advisories/cvrf/cve/{cve_id} | 
*DefaultApi* | [**securityAdvisoriesCvrfLatestNumberGet**](docs/DefaultApi.md#securityAdvisoriesCvrfLatestNumberGet) | **GET** /security/advisories/cvrf/latest/{number} | 
*DefaultApi* | [**securityAdvisoriesCvrfProductGet**](docs/DefaultApi.md#securityAdvisoriesCvrfProductGet) | **GET** /security/advisories/cvrf/product | 
*DefaultApi* | [**securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**](docs/DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/firstpublished | 
*DefaultApi* | [**securityAdvisoriesCvrfSeveritySeverityGet**](docs/DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityGet) | **GET** /security/advisories/cvrf/severity/{severity} | 
*DefaultApi* | [**securityAdvisoriesCvrfSeveritySeverityLastpublishedGet**](docs/DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityLastpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/lastpublished | 
*DefaultApi* | [**securityAdvisoriesCvrfYearYearGet**](docs/DefaultApi.md#securityAdvisoriesCvrfYearYearGet) | **GET** /security/advisories/cvrf/year/{year} | 
*DefaultApi* | [**securityAdvisoriesIosGet**](docs/DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios | 
*DefaultApi* | [**securityAdvisoriesIosxeGet**](docs/DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe | 
*DefaultApi* | [**securityAdvisoriesOvalAdvisoryAdvisoryIdGet**](docs/DefaultApi.md#securityAdvisoriesOvalAdvisoryAdvisoryIdGet) | **GET** /security/advisories/oval/advisory/{advisory_id} | 
*DefaultApi* | [**securityAdvisoriesOvalAllGet**](docs/DefaultApi.md#securityAdvisoriesOvalAllGet) | **GET** /security/advisories/oval/all | 
*DefaultApi* | [**securityAdvisoriesOvalCveCveIdGet**](docs/DefaultApi.md#securityAdvisoriesOvalCveCveIdGet) | **GET** /security/advisories/oval/cve/{cve_id} | 
*DefaultApi* | [**securityAdvisoriesOvalLatestNumberGet**](docs/DefaultApi.md#securityAdvisoriesOvalLatestNumberGet) | **GET** /security/advisories/oval/latest/{number} | 
*DefaultApi* | [**securityAdvisoriesOvalProductGet**](docs/DefaultApi.md#securityAdvisoriesOvalProductGet) | **GET** /security/advisories/oval/product | 
*DefaultApi* | [**securityAdvisoriesOvalSeveritySeverityFirstpublishedGet**](docs/DefaultApi.md#securityAdvisoriesOvalSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/firstpublished | 
*DefaultApi* | [**securityAdvisoriesOvalSeveritySeverityGet**](docs/DefaultApi.md#securityAdvisoriesOvalSeveritySeverityGet) | **GET** /security/advisories/oval/severity/{severity} | 
*DefaultApi* | [**securityAdvisoriesOvalSeveritySeverityLastpublishedGet**](docs/DefaultApi.md#securityAdvisoriesOvalSeveritySeverityLastpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/lastpublished | 


## Documentation for Models



## Documentation for Authorization

Authentication schemes defined for the API:
### psirt_openvuln_api_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorizatoin URL**: https://cloudsso.cisco.com/as/token.oauth2
- **Scopes**: 
  - read:cvrf: read cvrf files
  - read:oval: read oval files


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

os@cisco.com

