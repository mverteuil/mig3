"""
WSGI config for mig3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mig3.settings")
application = WhiteNoise(get_wsgi_application(), root=os.getenv("STATIC_ROOT", BASE_DIR / "staticfiles"))
