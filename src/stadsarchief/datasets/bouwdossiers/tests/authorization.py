import time

from django.conf import settings

from jwcrypto.jwt import JWT
from authorization_django.jwks import get_keyset


class AuthorizationSetup(object):
    """
    Helper methods to setup JWT tokens and authorization levels

    sets the following attributes:

    token_scope_hr_r
    """

    def setUpAuthorization(self):
        """
        SET

        token_scope_bd_r

        to use with:

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_bd_r))

        """
        jwks = get_keyset()
        assert len(jwks['keys']) > 0

        key = next(iter(jwks['keys']))
        now = int(time.time())

        header = {
            'alg': 'ES256',  # algorithm of the test key
            'kid': key.key_id
        }

        token = JWT(
            header=header,
            claims={
                'iat': now,
                'exp': now + 600,
                'scopes': [settings.SCOPE_BD_R]
            }
        )
        token.make_signed_token(key)
        self.token_scope_bd_r = token.serialize()
