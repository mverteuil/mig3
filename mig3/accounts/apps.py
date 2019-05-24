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
            secret_code = URLSignature.generate_signature()
            admin_url = f"http://localhost:8000{reverse('create_admin', kwargs={'secret_code': secret_code})}"
            message = (
                f"Please visit this SECRET URL in the next 10 minutes and create your administrator account: {admin_url}"
                if settings.DEBUG
                else f"Use this SECRET CODE in the next 10 minutes to create your administrator account: {secret_code}"
            )
            errors.append(checks.Warning(message, id="accounts.W001", obj=user_model))
    except ProgrammingError:
        pass  # Migrations have not run yet.
    return errors
