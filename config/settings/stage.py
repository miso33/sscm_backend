from .base import *

DEBUG = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
JWT_AUTH_COOKIE = "my-app-auth"
LOGIN_URL = env("LOGIN_URL")

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]
