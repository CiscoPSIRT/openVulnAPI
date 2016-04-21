# Description: Script to pull data from Cisco PSIRT openVuln API
# 
#
# Author: Derek Santos derekhalo@gmail.com
# Version: 0.1.20160420
#
# Requirements:
#  - Python version 3
#  - oauth2 - sudo pip3 install oauth2
#  - oauth2 - sudo pip3 install request

import oauth2 as oauth
import json, urllib.request, sys
 
print('Connecting to Cisco...')
 
consumer = oauth.Consumer(key="a9cbj36qsf4v7txnv9ymaqn6",secret="taTsuwtsrAxtkDU6WkyCNYyQ")
 
request_token_url = "https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=a9cbj36qsf4v7txnv9ymaqn6&client_secret=taTsuwtsrAxtkDU6WkyCNYyQ"
 
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




url = "https://api.cisco.com/security/advisories/"

if sys.argv[1] == "-cvrf":
    url = url + "cvrf/"

    if sys.argv[2] == "-all":
        url = url + "all/"
    elif sys.argv[2] == "-cve":
        url = url + "cve/" + sys.argv[3]
    elif sys.argv[2] == "-advisory":
        url = url + "advisory/" + sys.argv[3]
    elif sys.argv[2] == "-severity":
        url = url + "severity/" + sys.argv[3]
    elif sys.argv[2] == "-year":
        url = url + "year/" + sys.argv[3]
    elif sys.argv[2] == "-latest":
        url = url + "latest/" + sys.argv[3]



elif sys.argv[1] == "-oval":
    url = url + "oval/"

    if sys.argv[2] == "-all" or sys.argv[2] == "-a":
        url = url + "all/"
    elif sys.argv[2] == "-cve":
        url = url + "cve/" + sys.argv[3]
    elif sys.argv[2] == "-advisory":
        url = url + "advisory/" + sys.argv[3]
    elif sys.argv[2] == "-latest":
        url = url + "latest/" + sys.argv[3]


elif sys.argv[1] == "--help" or sys.argv[1] == "--h" or sys.argv[1] == "-h" or sys.argv[1] == "-help":
    print("THIS IS HELP")



req = urllib.request.Request(url)
req.add_header('Accept','application/json')
req.add_header('Authorization','Bearer '+j['access_token'])


resp = urllib.request.urlopen(req)
adv = resp.read()

advdata = json.loads(adv.decode('utf-8'))

#print (advdata)
for advisory in advdata['advisories']:
    print(advisory)





