import logging

from django.apps import AppConfig, apps
from django.conf import settings
from django.core.checks import Warning, register
from django.urls import reverse

from accounts.utils import URLSignature

logger = logging.getLogger(__name__)


class AccountsConfig(AppConfig):
    """User and API consumer account and authentication details."""

    name = "accounts"


@register()
def check_for_missing_administrator_account(app_configs, **kwargs):
    """Check for an existing administrator account and provide a bootstrapping URL if missing."""
    errors = []
    user_model = apps.get_model("accounts", "UserAccount", require_ready=True)
    if not user_model.objects.filter(is_superuser=True).count() > 0:
        host = "http://localhost:8000" if settings.DEBUG else "https://your-site.heroku.com"
        create_admin_url = reverse("create_admin", kwargs={"secret": URLSignature.generate_signature()})
        errors.append(
            Warning(
                f"Please visit this URL and create your administrator account: {host}{create_admin_url}",
                id="accounts.W001",
                obj=user_model,
            )
        )
    return errors
