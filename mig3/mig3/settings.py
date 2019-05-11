"""
Django settings for mig3 project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from distutils.util import strtobool
from pathlib import Path

import dj_database_url
import dotenv

# Environment variable utilities
# ------------------------------

getenv: callable = os.getenv
getenv_boolean: callable = lambda k, default=None: bool(strtobool(getenv(k, str(default))))
getenv_list: callable = lambda k, default=None: list(map(lambda s: s.strip(), getenv(k, default).split(",")))
getenv_int: callable = lambda k, default=None: int(getenv(k, default))

# Load environment variables from disk

dotenv.load_dotenv(dotenv.find_dotenv(), verbose=True)

# Build paths inside the project like this: BASE_DIR / "subdir" / "subdir"

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
BACKEND_DIR: Path = BASE_DIR / "mig3"
FRONTEND_DIR: Path = BASE_DIR / "mig3-ui"
FRONTEND_DIST_DIR: Path = FRONTEND_DIR / "dist"
TEMPLATES_DIR: Path = BACKEND_DIR / "templates"

# Secret Key
# https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY: str = getenv("SECRET_KEY")

# Debug
# https://docs.djangoproject.com/en/2.2/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG: bool = getenv_boolean("DEBUG", False)

# Allowed Hosts
# https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts

ALLOWED_HOSTS: list = getenv_list("ALLOWED_HOSTS")

# Sites Framework
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/#enabling-the-sites-framework

SITE_ID: int = 1

# Application definition
# https://docs.djangoproject.com/en/2.2/ref/settings/#installed-apps

INSTALLED_APPS: list = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_extensions",
    "django_fsm",
    "drf_yasg",
    "rest_framework",
    "webpack_loader",
    "accounts",
    "builds",
    "projects",
]

# Middleware
# https://docs.djangoproject.com/en/2.2/ref/settings/#middleware

MIDDLEWARE: list = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL Routing Root
# https://docs.djangoproject.com/en/2.2/ref/settings/#root-urlconf

ROOT_URLCONF: str = "mig3.urls"

# Append '/' to URLs if they're not included
# https://docs.djangoproject.com/en/2.2/ref/settings/#append-slash

APPEND_SLASH: bool = True

# Templates
# https://docs.djangoproject.com/en/2.2/ref/settings/#templates

TEMPLATES: list = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": getenv_list("TEMPLATE_DIRS") + [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Email Backend
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-backend

EMAIL_BACKEND: str = getenv("EMAIL_BACKEND", "django.core.mail.backends.filebased.EmailBackend")

# Email File Path
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-file-path

EMAIL_FILE_PATH: Path = BASE_DIR / "logs" / "emails-sent"

# Default Sender (email address)
# https://docs.djangoproject.com/en/2.2/ref/settings/#default-from-email

DEFAULT_FROM_EMAIL: str = "admin@example.com"

# WSGI Application Entry Point
# https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application

WSGI_APPLICATION: str = "mig3.wsgi.application"

# Databases
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES: dict = {"default": dj_database_url.parse(getenv("DATABASE_URL"))}

# Django Custom User Model
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL: str = "accounts.UserAccount"

# Authentication Backends
# https://docs.djangoproject.com/en/2.2/ref/settings/#authentication-backends

AUTHENTICATION_BACKENDS: list = ["django.contrib.auth.backends.ModelBackend"]

# Logging
# https://docs.djangoproject.com/en/2.2/ref/settings/#logging

LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "DEBUG", "handlers": ["console"]},
    "formatters": {"verbose": {"format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"}},
    "handlers": {"console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"}},
    "loggers": {"django.db.backends": {"level": "ERROR", "propagate": True}},
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: list = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Login URL route name
# https://docs.djangoproject.com/en/2.2/ref/settings/#login-url

LOGIN_URL: str = "admin:login"

# Post-login redirect URL route name
# https://docs.djangoproject.com/en/2.2/ref/settings/#login-redirect-url

LOGIN_REDIRECT_URL: str = "projects"

# Post-logout redirect URL route name
# https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.views.LogoutView
LOGOUT_REDIRECT_URL: str = "login"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# Language Code
# https://docs.djangoproject.com/en/2.2/ref/settings/#language-code

LANGUAGE_CODE: str = "en-us"

# Server Timezone
# https://docs.djangoproject.com/en/2.2/ref/settings/#time-zone

TIME_ZONE: str = "UTC"

# Use Internationalization
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-i18n

USE_I18N: bool = True

# Use Localization
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-l10n

USE_L10N: bool = True

# Use Timezone-aware Datetimes
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-tz

USE_TZ: bool = True

# Default file storage class to be used for any file-related operations that don’t specify a particular storage system.
# https://docs.djangoproject.com/en/2.2/ref/settings/#default-file-storage

DEFAULT_FILE_STORAGE: str = "django.core.files.storage.FileSystemStorage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# The file storage engine to use when collecting static files with the collectstatic management command.
# https://docs.djangoproject.com/en/2.2/ref/settings/#staticfiles-storage

STATICFILES_STORAGE: str = "django.contrib.staticfiles.storage.StaticFilesStorage"

# URL to use when referring to static files located in STATIC_ROOT
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-url

STATIC_URL: str = "/static/"

# Additional paths to to traverse if FileSystemFinder is enabled
# https://docs.djangoproject.com/en/2.2/ref/settings/#staticfiles-dirs

STATICFILES_DIRS: list = []

# --------------------------------------------------------------------------------------------------------------------
# Third-party Settings
# --------------------------------------------------------------------------------------------------------------------

# Django CORS Headers
# https://github.com/ottoyiu/django-cors-headers/

# Whitelist
# https://github.com/ottoyiu/django-cors-headers/#cors_origin_whitelist

CORS_ORIGIN_WHITELIST = ["http://localhost:8000", "http://localhost:8080"]

# Restrict Headers to matching regex
# https://github.com/ottoyiu/django-cors-headers/#cors_urls_regex

CORS_URLS_REGEX = r"^/api/.*$"

# Hash ID Field
# https://github.com/nshafer/django-hashid-field/

HASHID_SALTS: dict = {
    "accounts.BuilderAccount": getenv("HASHID_SALT_ACCOUNTS_BUILDER_ACCOUNT", "abc123"),
    "accounts.UserAccount": getenv("HASHID_SALT_ACCOUNTS_USER_ACCOUNT", "abc123"),
    "builds.Build": getenv("HASHID_SALT_BUILDS_BUILD", "abc123"),
    "projects.Project": getenv("HASHID_SALT_PROJECTS_PROJECT", "abc123"),
    "projects.Target": getenv("HASHID_SALT_PROJECTS_TARGET", "abc123"),
}

# Django REST Framework
# https://www.django-rest-framework.org/api-guide/

REST_FRAMEWORK: dict = {
    # Authentication classes
    # https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes
    "DEFAULT_AUTHENTICATION_CLASSES": ("api.authentication.BearerAuthentication",),
    # Lock down permissions by default
    # https://www.django-rest-framework.org/api-guide/settings/#default_permission_classes
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAdminUser",),
    # Override Django request factory comptability default
    # https://www.django-rest-framework.org/api-guide/testing/#setting-the-default-format
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

# Django Webpack Loader
# https://github.com/owais/django-webpack-loader#configuration

WEBPACK_LOADER = {
    "DEFAULT": {
        # Cache
        # https://github.com/owais/django-webpack-loader#cache
        "CACHE": not DEBUG,
        # Bundle Directory (must end with slash)
        # https://github.com/owais/django-webpack-loader#bundle_dir_name
        "BUNDLE_DIR_NAME": "/bundles/",
        # Webpack Stats File
        # https://github.com/owais/django-webpack-loader#stats_file
        "STATS_FILE": FRONTEND_DIST_DIR / "webpack-stats.json",
    }
}

# DRF-YASG
# https://drf-yasg.readthedocs.io/en/stable/

SWAGGER_SETTINGS: dict = {
    # Bearer token only
    # https://drf-yasg.readthedocs.io/en/stable/security.html?highlight=Bearer#security-definitions
    "SECURITY_DEFINITIONS": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}}
}
