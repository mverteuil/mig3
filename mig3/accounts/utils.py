from __future__ import annotations

from datetime import timedelta
from typing import Union

from django.conf import settings
from django.core import signing


class URLSignature:
    """Generate and validate secret for use in temporary URLs."""

    @staticmethod
    def generate_signature(value: str = "check") -> str:
        """Generate a secret for use in the url, which can be checked for expiry."""
        signer = signing.TimestampSigner(salt=settings.SECRET_URL_SALT)
        secret = signer.sign(value)
        return secret

    @staticmethod
    def validate_signature(secret: str, max_age: Union[int, timedelta] = None, value: str = "check") -> bool:
        """Validate that a secret contains the expected value and that it has not expired if necessary."""
        try:
            signer = signing.TimestampSigner(salt=settings.SECRET_URL_SALT)
            result = signer.unsign(secret, max_age=max_age)
            return result == value
        except (signing.BadSignature, signing.SignatureExpired):
            return False
