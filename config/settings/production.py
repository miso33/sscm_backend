from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from django.core.exceptions import DisallowedHost

ignore_errors = (DisallowedHost,)
DEBUG = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
JWT_AUTH_COOKIE = "my-app-auth"
LOGIN_URL = env("LOGIN_URL")


def before_send(event, hint):
    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, ignore_errors):
            return None
    return event


sentry_sdk.init(
    dsn="https://90e4eabab75c4759a662b02a0d5887f1@o1085724.ingest.sentry.io/6096984",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
    before_send=before_send,
)
SERVER_EMAIL = env("EMAIL_HOST_USER")

ADMINS = [("admin", "reports@scrypta.sk")]
