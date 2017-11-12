IPS_SIGNATURE_LABEL = 'ips_signatures'

API_LABELS = (
    'advisory_id',
    'advisory_title',
    'bug_ids',
    'cves',
    'cvrf_url',
    'cvss_base_score',
    'cwe',
    'first_fixed',
    'first_published',
    'ios_release',
    IPS_SIGNATURE_LABEL,
    'last_updated',
    'oval_url',
    'product_names',
    'publication_url',
    'sir',
    'summary',
)

IPS_SIGNATURES = (
    'legacy_ips_id',
    'legacy_ips_url',
    'release_version',
    'software_version',
)

ALLOWS_FILTER = (
    'all',
    'severity',
)

NA_INDICATOR = 'NA'

JSON_OUTPUT_FORMAT_TOKEN = 'json'
CSV_OUTPUT_FORMAT_TOKEN = 'csv'

CVRF_ADVISORY_FORMAT_TOKEN = 'cvrf'
OVAL_ADVISORY_FORMAT_TOKEN = 'oval'
IOS_ADVISORY_FORMAT_TOKEN = 'ios'

ADVISORY_FORMAT_TOKENS = (
    CVRF_ADVISORY_FORMAT_TOKEN,
    OVAL_ADVISORY_FORMAT_TOKEN,
    IOS_ADVISORY_FORMAT_TOKEN,
)
