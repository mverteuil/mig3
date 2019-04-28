import secrets

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from hashid_field import HashidAutoField
from model_utils.models import TimeStampedModel


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError("Email is a required field.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return super().get_by_natural_key(email)


class UserAccount(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """Authenticate and authorize users."""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["accounts.UserAccount"])
    email = models.EmailField(
        "Email Address",
        unique=True,
        help_text=(
            "NOTE: You must use the email address associated with their git commits to correctly attach submissions "
            "to respective user accounts."
        ),
    )
    name = models.CharField("Name", max_length=254, blank=True)
    is_staff = models.BooleanField(
        "Staff status", default=False, help_text="Designates whether the user can log into the admin site."
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )

    objects = UserAccountManager()

    EMAIL_FIELD = USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}{'†' if self.is_staff else '￿'}{'*' if self.is_superuser else ''} ({self.id})"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class BuilderAccount(TimeStampedModel):
    """Authorize builders to submit job results"""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["accounts.BuilderAccount"])
    name = models.CharField("Name", max_length=254, help_text="Suggestions: CircleCI, TravisCI, Jenkins, etc.")
    token = models.CharField(
        "Bearer Token", max_length=64, default=secrets.token_hex, help_text="Used for builder request authentication."
    )

    def __str__(self):
        return f"{self.name} ({self.id})"
