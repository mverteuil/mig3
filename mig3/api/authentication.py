from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from accounts import models as accounts


class BearerAuthentication(TokenAuthentication):
    """Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Bearer ".  For example:

        Authorization: Bearer 401f7ac837da42b97f613d789819ff93537bee6a

    """

    keyword: str = "Bearer"
    model: models.Model = accounts.BuilderAccount

    def authenticate_credentials(self, token: str) -> (AnonymousUser, accounts.BuilderAccount):
        """Find associated BuilderAccount for authentication token, if it exists."""
        model = self.get_model()
        try:
            builder = model.objects.get(token=token)
        except ObjectDoesNotExist:
            raise AuthenticationFailed("Invalid token.")

        return AnonymousUser(), builder
