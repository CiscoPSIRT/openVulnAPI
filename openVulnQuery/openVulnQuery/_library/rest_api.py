"""
Below API in sync with swagger YAML file documented as of:
    API version: 0.0.3,
    Commit timestamp: 2017-01-21 05:47 UTC
    Commit revision: 61dd61b23124d6d314aa3c844b7e33e67b3a5d76

schemes:
 - https
host: api.cisco.com

securityDefinitions:
  psirt_openvuln_api_auth:
    type: oauth2
    authorizationUrl: 'https://cloudsso.cisco.com/as/token.oauth2'
    flow: implicit
    scopes:
      'read:cvrf': read cvrf files
      'read:oval': read oval files

produces:
  - application/json

methods/paths:

    Method(s): GET

    API Root: /security/advisories/

        Advisory Format Path(s):

            CVRF: cvrf/

                CVRF unary only:

                CVRF binary-only:

                    all  # JSON (default)
                    all.xml  # To obtain the output in XML (CVRF v1.1)
                    product?product

                CVRF ternary:

                    advisory/{advisory_id}
                    cve/{cve_id}
                    latest/{number}

                    severity/{severity}

                    severity/{severity}/firstpublished?(startDate,endDate)
                    severity/{severity}/lastpublished?(startDate,endDate)

                    year/{year}

            OVAL: oval/

                OVAL unary only:

                OVAL binary-only:

                    all  # JSON (default)
                    all.xml  # To obtain the output in XML (OVAL)
                    product?product

                OVAL ternary:

                    advisory/{advisory_id}
                    cve/{cve_id}
                    latest/{number}

                    severity/{severity}

                    severity/{severity}/firstpublished?(startDate,endDate)
                    severity/{severity}/lastpublished?(startDate,endDate)

                    # Note: There is no year entity entry point in OVAL!

            IOS:

                IOS unary only:

                    ios?version
                    iosxe?version

path parameter dict (for ternary paths):

        - name: cve_id
          in: path
          description: 'CVE Identifier (i.e., CVE-YYYY-NNNN)'
          required: true
          type: string
          format: CVE-YYYY-NNNN

        - name: advisory_id
          in: path
          description: advisory ID
          required: true
          type: string
          format: cisco-sa-XXX

        - name: severity
          in: path
          description: Critical, High, Medium, Low
          required: true
          type: string
          enum:
            - critical
            - high
            - medium
            - low
          format: enum

        - name: year
          in: path
          description: The four digit year.
          required: true
          type: string
          format: YYYY

        - name: number
          in: path
          description: An absolute number to obtain the latest security|
                       advisories.
          required: true
          type: integer
          format: number

query parameter dict (for ternary paths):

        - name: startDate
          in: query
          required: true
          type: string
          format: date

        - name: endDate
          in: query
          required: true
          type: string
          format: date

        - name: product
          in: query
          description: A[] product name to obtain security advisories that|
                       match given product name.
          required: true
          type: string
          format: string

        - name: version
          in: query
          description: IOS version to obtain security advisories
          required: true
          type: string
          format: string

terms:
  CVRF - Common Vulnerability Reporting Format
  OVAL - Open Vulnerability and Assessment Language

"""

MIME_TYPE = 'application/json'


def rest_with_auth_headers(auth_token, user_agent):
    """Construct per session for sending with all GET requests to API."""
    return {
        'Authorization': 'Bearer {}'.format(auth_token),
        'Accept': MIME_TYPE,
        'User-Agent': user_agent,
    }
