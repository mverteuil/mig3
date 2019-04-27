import secrets

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from hashid_field import HashidAutoField
from model_utils.models import TimeStampedModel


class UserAccount(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """Authenticate and authorize users."""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["HASHID_SALT_ACCOUNTS_USER_ACCOUNT"])
    email = models.EmailField(
        "Email Address",
        help_text=(
            "NOTE: You must use the email address associated with their git commits to correctly attach submissions "
            "to respective user accounts."
        ),
    )
    name = models.CharField("Name", max_length=254, blank=True)
    is_staff = models.BooleanField(default=False, help_text="Designates whether the user can log into the admin site.")
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class BuilderAccount(TimeStampedModel):
    """Authorize builders to submit job results"""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["HASHID_SALT_ACCOUNTS_BUILDER_ACCOUNT"])
    name = models.CharField("Name", max_length=254, help_text="Suggestions: CircleCI, TravisCI, Jenkins, etc.")
    token = models.CharField(
        "Bearer Token", max_length=40, default=secrets.token_hex, help_text="Used for builder request authentication."
    )
