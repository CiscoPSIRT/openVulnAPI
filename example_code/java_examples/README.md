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
            apiInstance.securityAdvisoriesAdvisoryAdvisoryIdGet(advisoryId);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#securityAdvisoriesAdvisoryAdvisoryIdGet");
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cisco.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**securityAdvisoriesAdvisoryAdvisoryIdGet**](docs/DefaultApi.md#securityAdvisoriesAdvisoryAdvisoryIdGet) | **GET** /security/advisories/advisory/{advisory_id} |
*DefaultApi* | [**securityAdvisoriesAllGet**](docs/DefaultApi.md#securityAdvisoriesAllGet) | **GET** /security/advisories/all |
*DefaultApi* | [**securityAdvisoriesCveCveIdGet**](docs/DefaultApi.md#securityAdvisoriesCveCveIdGet) | **GET** /security/advisories/cve/{cve_id} |
*DefaultApi* | [**securityAdvisoriesIosGet**](docs/DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios |
*DefaultApi* | [**securityAdvisoriesIosxeGet**](docs/DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe |
*DefaultApi* | [**securityAdvisoriesLatestNumberGet**](docs/DefaultApi.md#securityAdvisoriesLatestNumberGet) | **GET** /security/advisories/latest/{number} |
*DefaultApi* | [**securityAdvisoriesProductGet**](docs/DefaultApi.md#securityAdvisoriesProductGet) | **GET** /security/advisories/product |
*DefaultApi* | [**securityAdvisoriesSeveritySeverityFirstpublishedGet**](docs/DefaultApi.md#securityAdvisoriesSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/severity/{severity}/firstpublished |
*DefaultApi* | [**securityAdvisoriesSeveritySeverityGet**](docs/DefaultApi.md#securityAdvisoriesSeveritySeverityGet) | **GET** /security/advisories/severity/{severity} |
*DefaultApi* | [**securityAdvisoriesSeveritySeverityLastpublishedGet**](docs/DefaultApi.md#securityAdvisoriesSeveritySeverityLastpublishedGet) | **GET** /security/advisories/severity/{severity}/lastpublished |
*DefaultApi* | [**securityAdvisoriesYearYearGet**](docs/DefaultApi.md#securityAdvisoriesYearYearGet) | **GET** /security/advisories/year/{year} |


## Documentation for Models



## Documentation for Authorization

Authentication schemes defined for the API:
### psirt_openvuln_api_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://cloudsso.cisco.com/as/token.oauth2
- **Scopes**:
  - read:advisories: read advisories


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

os@cisco.com
