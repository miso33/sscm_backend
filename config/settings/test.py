from .base import *

# GENERAL

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = []


# ACCOUNT

ACCOUNT_EMAIL_VERIFICATION = "none"

# PASSWORD

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
