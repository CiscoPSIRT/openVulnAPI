The following are step-by-step instructions on how to access the Cisco PSIRT openVuln API.
 
Step 1: Access the Cisco API console at: https://apiconsole.cisco.com

Step 2: Login with your CCO credentials (login is only available to registered Cisco customers and partners).

Step 3: Register your application and obtain your client credentials.

Step 4: Once you register your application and obtain your client ID and client secret, the next step is to obtain an authorization token. Authorization tokens in the Cisco PSIRT openVuln API are valid for one (1) hour. The following example demonstrates how to get the token using the curl utility.

```
curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=<client_id>" -d "client_secret=<client_secret>" -d "grant_type=client_credentials" https://cloudsso.cisco.com/as/token.oauth2
```

For example:
```
omar@omar:~$ curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id= XXXXXXXX" -d "client_secret=YYYYYYYY" -d "grant_type=client_credentials" https://cloudsso.cisco.com/as/token.oauth2
{"access_token":"ytuopLCGZxBFN5O0hnL1M2QX2QVp","token_type":"Bearer","expires_in":3599}
```

Step 5: Make API calls to https://api.cisco.com/security/... The following example uses the curl command to retrieve CVRF files for all Cisco Security Advisories.
```
curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer uayEoKBrv0nfjrUavwix1ye8ZoNO" https://api.cisco.com/security/advisories/cvrf/all
```
The following example demonstrates how to obtain the latest 10 advisories:
```
curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer uayEoKB
rv0nfjrUavwix1ye8ZoNO" https://api.cisco.com/security/advisories/cvrf/latest/10
```
For more information about the available RESTful resource URIs and the Cisco PSIRT openVuln API visit: https://developer.cisco.com/site/PSIRT/

