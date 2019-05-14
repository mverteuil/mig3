import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class AccountsConfig(AppConfig):
    """User and API consumer account and authentication details."""

    name = "accounts"

    def ready(self):
        """Perform checks on application load."""
        user_model = self.get_model("UserAccount", True)
        if not user_model.objects.count():
            logger.info(
                "You have not created an administrator account yet. Please visit this URL and create the administrator account: %URL%"
            )
