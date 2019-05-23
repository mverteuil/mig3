import logging

from django.apps import AppConfig, apps
from django.conf import settings
from django.core import checks
from django.db import ProgrammingError
from django.urls import reverse

from accounts.utils import URLSignature

logger = logging.getLogger(__name__)


class AccountsConfig(AppConfig):
    """User and API consumer account and authentication details."""

    name = "accounts"


@checks.register()
def check_for_missing_administrator_account(app_configs, **kwargs):
    """Check for an existing administrator account and provide a bootstrapping URL if missing."""
    errors = []
    user_model = apps.get_model("accounts", model_name="UserAccount")
    try:
        if not user_model.objects.filter(is_superuser=True).count() > 0:
            host = "http://localhost:8000" if settings.DEBUG else "https://your-app-name.herokuapp.com"
            create_admin_url = reverse("create_admin", kwargs={"secret": URLSignature.generate_signature()})
            errors.append(
                checks.Warning(
                    f"Please visit this URL and create your administrator account: {host}{create_admin_url}",
                    id="accounts.W001",
                    obj=user_model,
                )
            )
    except ProgrammingError:
        pass  # Migrations have not run yet.
    return errors
