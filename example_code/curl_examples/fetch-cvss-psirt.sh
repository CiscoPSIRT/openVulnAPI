#!/bin/sh

CLIENTID="${1}"
CLIENTSECRET="${2}"

bearertoken="$(curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=${CLIENTID}" -d "client_secret=${CLIENTSECRET}" -d "grant_type=client_credentials" https://cloudsso.cisco.com/as/token.oauth2 | cut -f 4 -d "\"")"
printf "bearer token: ${bearertoken}\n"
curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer ${bearertoken}" https://api.cisco.com/security/advisories/all | tr "," "\n" | grep -i "cvrf" | cut -f 4 -d "\"" | while read advisoryurl
do
	curl "${advisoryurl}" | grep -i "cvss"
done
