# cisco_psirt_open_vuln_api

CiscoPsirtOpenVulnApi - JavaScript client for cisco_psirt_open_vuln_api
The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). For more information about the Cisco PSIRT openVuln API visit https://developer.cisco.com/psirt  

For detail steps on how to use the API go to: https://developer.cisco.com/psirt  This is a beta release of a swagger YAML for the Cisco PSIRT openVuln API  To access the API sign in with your Cisco CCO account at http://apiconsole.cisco.com and register an application to receive a client_id and a client_secret .


## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install cisco_psirt_open_vuln_api --save
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing
into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

Finally, switch to the directory you want to use your cisco_psirt_open_vuln_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

You should now be able to `require('cisco_psirt_open_vuln_api')` in javascript files from the directory you ran the last
command above from.

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/YOUR_USERNAME/cisco_psirt_open_vuln_api
then install it via:

```shell
    npm install YOUR_USERNAME/cisco_psirt_open_vuln_api --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CiscoPsirtOpenVulnApi = require('cisco_psirt_open_vuln_api');

var defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;

// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
var psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = "YOUR ACCESS TOKEN"

var api = new CiscoPsirtOpenVulnApi.DefaultApi()

var advisoryId = "advisoryId_example"; // {String} advisory ID


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.securityAdvisoriesAdvisoryAdvisoryIdGet(advisoryId, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cisco.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesAdvisoryAdvisoryIdGet**](docs/DefaultApi.md#securityAdvisoriesAdvisoryAdvisoryIdGet) | **GET** /security/advisories/advisory/{advisory_id} |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesAllGet**](docs/DefaultApi.md#securityAdvisoriesAllGet) | **GET** /security/advisories/all |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesCveCveIdGet**](docs/DefaultApi.md#securityAdvisoriesCveCveIdGet) | **GET** /security/advisories/cve/{cve_id} |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesIosGet**](docs/DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesIosxeGet**](docs/DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesLatestNumberGet**](docs/DefaultApi.md#securityAdvisoriesLatestNumberGet) | **GET** /security/advisories/latest/{number} |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesProductGet**](docs/DefaultApi.md#securityAdvisoriesProductGet) | **GET** /security/advisories/product |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesSeveritySeverityFirstpublishedGet**](docs/DefaultApi.md#securityAdvisoriesSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/severity/{severity}/firstpublished |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesSeveritySeverityGet**](docs/DefaultApi.md#securityAdvisoriesSeveritySeverityGet) | **GET** /security/advisories/severity/{severity} |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesSeveritySeverityLastpublishedGet**](docs/DefaultApi.md#securityAdvisoriesSeveritySeverityLastpublishedGet) | **GET** /security/advisories/severity/{severity}/lastpublished |
*CiscoPsirtOpenVulnApi.DefaultApi* | [**securityAdvisoriesYearYearGet**](docs/DefaultApi.md#securityAdvisoriesYearYearGet) | **GET** /security/advisories/year/{year} |


## Documentation for Models



## Documentation for Authorization


### psirt_openvuln_api_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://cloudsso.cisco.com/as/token.oauth2
- **Scopes**:
  - read:advisories: read advisories
