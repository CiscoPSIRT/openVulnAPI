# There are four prerequisites needed before a user can initiate the API service calls and obtain access to the underlying Cisco security vulnerability information.
#  - Sign-in with your CCO ID
#  - Register a client application to create a “unique client identifier” that will identify your client application to the Cisco Token services. Registration creates the client credentials along with name assignment, description, and subscribes the client application to one or more of the OAuth v2.0 grant types requested for their client  application.
#  - Get Access Tokens - utilize Cisco's Token services to acquire an OAuth v2.0 access-token(s).
#  - Make API Calls

# Enter your client ID and client secret below.  

CLIENT_ID = ""
CLIENT_SECRET = ""

REQUEST_TOKEN_URL = "https://cloudsso.cisco.com/as/token.oauth2"
API_URL = "https://api.cisco.com/security/advisories"
