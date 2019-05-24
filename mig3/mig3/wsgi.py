"""
WSGI config for mig3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import logging
import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

logger = logging.getLogger(__name__)

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mig3.settings")
application = WhiteNoise(get_wsgi_application(), root=os.getenv("STATIC_ROOT", BASE_DIR / "staticfiles"))
logger.debug("WSGI Application loaded.")
