import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
app = Celery("proj")
app.conf.broker_url = "redis://localhost:6379/0"
app.autodiscover_tasks(settings.INSTALLED_APPS)
task = app.task
