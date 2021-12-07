from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
JWT_AUTH_COOKIE = "my-app-auth"
LOGIN_URL = env("LOGIN_URL")

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

sentry_sdk.init(
    dsn="https://90e4eabab75c4759a662b02a0d5887f1@o1085724.ingest.sentry.io/6096984",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
SERVER_EMAIL = env("EMAIL_HOST_USER")

ADMINS = [("admin", "reports@scrypta.sk")]
