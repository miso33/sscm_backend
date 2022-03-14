from celery import shared_task
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime

from sscm.notifications.models import Notification
from sscm.profiles.models import IndividualProfile, MemberProfile


@shared_task(name='create_birthday_emails')
def create_birthday_list_emails():
    pass
    # individual_profiles = IndividualProfile.objects.filter(
    #     birth_date__month=datetime.now().month + 1
    # ).order_by(
    #     "birth_date"
    # )
    # member_profiles = MemberProfile.objects.filter(
    #     individual_profile__birth_date__month=datetime.now().month + 1
    # ).order_by(
    #     "individual_profile__birth_date"
    # )
    # print(member_profiles)
    # if member_profiles.exists():
    #     Notification.objects.create(
    #         recipients=["pokus"],
    #         body=render_to_string(
    #             "birthday_list_email.html",
    #             {
    #                 "profiles": member_profiles.values(
    #                     "individual_profile__first_name",
    #                     "individual_profile__last_name", "individual_profile__birth_date"
    #                 )
    #             }
    #         )
    #     )


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
