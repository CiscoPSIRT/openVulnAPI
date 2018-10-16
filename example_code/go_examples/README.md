# Go API client for Cisco PSIRT openVuln API

The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information).

For more information about the Cisco PSIRT openVuln API visit https://developer.cisco.com/site/PSIRT/discover/overview  For detail steps on how to use the API go to: https://developer.cisco.com/site/PSIRT/get-started/getting-started.gsp  This is a beta release of a swagger YAML for the Cisco PSIRT openVuln API  To access the API sign in with your Cisco CCO account at http://apiconsole.cisco.com and register an application to receive a client_id and a client_secret.

To obtain client ID and client secret:

1. Visit <https://apiconsole.cisco.com/>
2. Sign In
3. Select My Applications Tab
4. Register a New Application by:

  - Entering Application Name
  - Under OAuth2.0 Credentials check Client Credentials
  - Under Select APIs choose Cisco PSIRT openVuln API
  - Agree to the terms and service and click Register

5. Take note of the "rate contract" presented like e.g.:

  ```
   Rate Limits
   10    Calls per second
   5,000    Calls per day
  ```

6. Note the value of "Client ID" (a string like e.g. 'abc12abcd13abcdefabcde1a')
7. Note the value of "Client Secret" (a string like e.g. '1a2abcDEfaBcDefAbcDeFA3b')


## Documentation for API Endpoints

For more information about the openVuln API and how to access it visit: https://developer.cisco.com/psirt


## Documentation For Authorization

## psirt_openvuln_api_auth
- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://cloudsso.cisco.com/as/token.oauth2
- **Scopes**:
 - **read:advisories**: read advisories

Example
```
	auth := context.WithValue(context.Background(), sw.ContextAccessToken, "ACCESSTOKENSTRING")
    r, err := client.Service.Operation(auth, args)
```

Or via OAuth2 module to automatically refresh tokens and perform user authentication.
```
	import 	"golang.org/x/oauth2"

    / .. Perform OAuth2 round trip request and obtain a token .. //

    tokenSource := oauth2cfg.TokenSource(createContext(httpClient), &token)
	auth := context.WithValue(oauth2.NoContext, sw.ContextOAuth2, tokenSource)
    r, err := client.Service.Operation(auth, args)
```
