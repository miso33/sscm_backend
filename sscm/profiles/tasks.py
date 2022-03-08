import pytest
from celery import shared_task
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime, date
from django.conf import settings

from sscm.notifications.models import Notification
from sscm.profiles.models import IndividualProfile


@pytest.mark.birthday_wish_email
@shared_task(name='create_birthday_emails')
def create_birthday_list_emails():
    individual_profiles = IndividualProfile.objects.filter(
        birth_date__month=datetime.now().month + 1
    ).order_by(
        "birth_date"
    )
    if individual_profiles.exists():
        Notification.objects.create(
            recipients=["pokus"],
            body=render_to_string(
                "birthday_list_email.html",
                {"profiles": individual_profiles.values("first_name", "last_name", "birth_date")}
            )
        )


@pytest.mark.birthday_wish_email
@shared_task(name='birthday_wish_email')
def create_birthday_wish_email():
    individual_profiles = IndividualProfile.objects.filter(
        birth_date=datetime.now()
    )
    if individual_profiles.exists():
        Notification.objects.create(
            recipients=[individual_profile.user.email for individual_profile in individual_profiles],
            body=render_to_string(
                "birthday_list_email.html",
                {"profiles": individual_profiles.values("first_name", "last_name", "birth_date")}
            )
        )
