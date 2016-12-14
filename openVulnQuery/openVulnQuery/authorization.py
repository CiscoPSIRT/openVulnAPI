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

    payload = {'client_id': client_id, 'client_secret': client_secret}
    data = {'grant_type' : "client_credentials"}
    r = requests.post(config.REQUEST_TOKEN_URL, params = payload, data = data)
    r.raise_for_status()
    resp = r.json()
    return resp['access_token']
