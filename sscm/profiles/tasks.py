from celery import shared_task
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime

from sscm.notifications.models import Notification
from sscm.profiles.models import IndividualProfile, MemberProfile


@shared_task(name='create_birthday_emails')
def create_birthday_list_emails():
    Notification.objects.create(
        recipients=["pokus"],
        subject="Narodeniny tento mesiac",
        body=render_to_string(
            "birthday_list_email.html",
            {
                "profiles": MemberProfile.objects.birthdays_by_month(datetime.now().month + 1)
            }
        )
    )


@shared_task(name='birthday_wish_email')
def create_birthday_wish_email():
    for member_profile in MemberProfile.objects.birthdays_by_day(datetime.now()):
        Notification.objects.create(
            recipients=[member_profile["email"]],
            subject="Všetko najlepšie k narodeninám",
            body=render_to_string(
                "birthday_list_email.html",
                {"profiles": member_profile}
            )
        )
