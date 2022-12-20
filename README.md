# Cisco PSIRT openVuln API

## Overview
The Cisco PSIRT openVuln API is a RESTful API that allows customers to obtain Cisco security vulnerability information in different machine-consumable formats. It supports industrywide security standards such as:
* OASIS Common Security Advisory Framework (CSAF) 
* Common Vulnerability and Exposure (CVE) identifiers
* Common Weakness Enumerator (CWE)
* Common Vulnerability Scoring System (CVSS)

**NOTE**: [CSAF](https://csaf.io) is a specification for structured machine-readable vulnerability-related advisories and further refine those standards over time. CSAF is the new name and replacement for the Common Vulnerability Reporting Framework (CVRF). Cisco will support CVRF until December 31, 2023. More information at: https://csaf.io 

The Cisco PSIRT openVuln API allows technical staff and programmers to build tools that help them do their job more effectively. In this case, it enables them to easily keep up with security vulnerability information specific to their network. That frees up more time for them to manage their network and deploy new capabilities in their infrastructure. The API also allows Cisco customers and partners to leverage machine readable data to keep-up with Cisco security advisories. It further simplifies the evaluation process and reduces the time between when a vulnerability is announced and the fix is actually implemented.

## API Documentation

For more information about the openVuln API and how to access it visit:
https://developer.cisco.com/psirt

## Community-Supported Python-based Client : openVulnQuery

The open-source community-supported [Python-based API client (openVulnQuery)](https://github.com/CiscoPSIRT/openVulnQuery) can be obtained from: https://github.com/CiscoPSIRT/openVulnQuery

## Docker Container
The client can be easily run in a container. For your convenience, a [Dockerfile is available](https://github.com/CiscoPSIRT/openVulnAPI/blob/master/openVulnQuery/Dockerfile) to run the client is a slim container running Alpine and Python 3.x.

You can also pull the container from [Docker Hub](https://hub.docker.com/r/santosomar/openvulnquery/) with:
```
docker pull santosomar/openvulnquery
```
