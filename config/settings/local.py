from .base import *

DEBUG = True
ACCOUNT_EMAIL_VERIFICATION = "none"
DRF_RECAPTCHA_TESTING_PASS = True
INSTALLED_APPS += ["django_extensions"]
ALLOWED_HOSTS = ["192.168.0.234", ".localhost", "127.0.0.1"]
