import requests

from . import config


def get_oauth_token(client_id, client_secret, request_token_url=None):
    """Get OAuth2 token from api based on client id and secret.

    :param client_id: Client id stored in config file.
    :param client_secret: Client secret stored in config file.
    :param request_token_url: the POST URL to request a token response

    :return The valid access token to pass to api in header.
    :raise requests exhibits anything other than a 200 response.

    """
    r = requests.post(
        request_token_url if request_token_url else config.REQUEST_TOKEN_URL,
        params={'client_id': client_id, 'client_secret': client_secret},
        data={'grant_type': 'client_credentials'}
    )
    r.raise_for_status()
    return r.json()['access_token']
