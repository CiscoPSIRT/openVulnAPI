# Cisco PSIRT openVuln API

## Overview
The Cisco PSIRT openVuln API is a RESTful API that allows customers to obtain Cisco security vulnerability information in different machine-consumable formats. It supports industrywide security standards such as the OASIS Common Security Advisory Framework (CSAF) Common Vulnerability Reporting Framework (CVRF), Common Vulnerability and Exposure (CVE) identifiers, Common Weakness Enumerator (CWE), and the Common Vulnerability Scoring System (CVSS).

This API allows technical staff and programmers to build tools that help them do their job more effectively. In this case, it enables them to easily keep up with security vulnerability information specific to their network. That frees up more time for them to manage their network and deploy new capabilities in their infrastructure.

The API also allows Cisco customers and partners to leverage machine readable data to keep-up with Cisco security advisories. It further simplifies the evaluation process and reduces the time between when a vulnerability is announced and the fix is actually implemented.

## API Documentation

For more information about the openVuln API and how to access it visit:
https://developer.cisco.com/psirt

## Python-based Client : openVulnQuery

The [Python-based API client (openVulnQuery)](https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery) can be installed using Python `pip`, as shown below:

```
pip install openVulnQuery
```

Depending on your environment, you may need to specify the latest version (1.30), as demonstrated below:

```
python3 -m pip install openVulnQuery==1.30
```

If you are experiencing any difficulty installing openVulnQuery. Here is the link to [common installation issues solutions](<https://github.com/iamparas/openVulnAPI/blob/master/openVulnQuery/InstallationIssueSolutions.md>).

The client source code can be accessed [here](https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery).

## Docker Container
The client can be easily run in a container. For your convenience, a [Dockerfile is available](https://github.com/CiscoPSIRT/openVulnAPI/blob/master/openVulnQuery/Dockerfile) to run the client is a slim container running Alpine and Python 3.x.

You can also pull the container from [Docker Hub](https://hub.docker.com/r/santosomar/openvulnquery/) with:
```
docker pull santosomar/openvulnquery
```
