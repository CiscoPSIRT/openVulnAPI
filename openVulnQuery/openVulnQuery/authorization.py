import requests

import config


def get_oauth_token(client_id, client_secret):
    """Get OAuth2 token from api based on client id and secret.

    Args:
        client_id: Client id stored in config file.
        client_secret: Client secret stored in config file.
    Returns:
        The valid access token to pass to api in header.
    Raises:
        If requests exhibits anything other than a 200 response.

    """
    r = requests.post(
        config.REQUEST_TOKEN_URL,
        params={'client_id': client_id, 'client_secret': client_secret},
        data={'grant_type': 'client_credentials'}
    )
    r.raise_for_status()
    return r.json()['access_token']
