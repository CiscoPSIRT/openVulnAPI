#!/usr/local/bin/python3

# Example python code to access the openVuln API
# Based on contributions from Ryan Ruckley
 
import oauth2 as oauth
import json
import urllib.request
 
print('Connecting to Cisco...')
 
consumer = oauth.Consumer(key="<yourClientID>",secret="<yourClientSecret>")
 
request_token_url = "https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=<yourClientID>&client_secret=<yourClientSecret>"
 
client = oauth.Client(consumer)
 
resp, content = client.request(request_token_url, "POST")
 
print(content)
 
j = json.loads(content.decode('utf-8'))

print('Access Token Retrieved...') 
print(j['access_token'])

# Replace the Request URL below with the openVuln REST API resource you would like to access.
# In this example, we are getting all advisories in CVRF format
# The available resources are documented at:
# https://developer.cisco.com/site/PSIRT/get-started/getting-started.gsp

req = urllib.request.Request('https://api.cisco.com/security/advisories/cvrf/year/2015')
req.add_header('Accept','application/json')
req.add_header('Authorization','Bearer '+j['access_token'])
resp = urllib.request.urlopen(req)
adv = resp.read()
 
advdata = json.loads(adv.decode('utf-8'))
 
 
for advisory in advdata['advisories']:
    print(advisory)
