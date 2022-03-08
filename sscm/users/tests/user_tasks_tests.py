from datetime import timedelta, datetime

import pytest
from dateutil.relativedelta import *
from django.contrib.auth import get_user_model
from django.urls import include, path

from sscm.core.tests import BaseAPITestCase
from sscm.notifications.models import Notification
from sscm.profiles.factories import IndividualProfileFactory
from sscm.profiles.tasks import create_birthday_wish_email, create_birthday_list_emails

User = get_user_model()


class UserTasksAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("account/registration/", include("dj_rest_auth.registration.urls")),
        path("account/", include("dj_rest_auth.urls")),
    ]

    @pytest.mark.notification
    @pytest.mark.birthday
    def test_create_birthday_list_emails(self):
        birthday_profiles = IndividualProfileFactory.create_batch(
            3,
            birth_date=datetime.now() + relativedelta(months=+1)
        )
        IndividualProfileFactory.create_batch(
            10,
            birth_date=datetime.now() + relativedelta(months=+2)
        )
        create_birthday_list_emails()
        for birthday_profile in birthday_profiles:
            self.assertIn(
                birthday_profile.birth_date.strftime("%d.%m.%Y"),
                Notification.objects.last().body
            )

    @pytest.mark.notification
    @pytest.mark.birthday
    def test_create_birthday_wish_emails(self):
        birthday_profiles = IndividualProfileFactory.create_batch(
            2,
            birth_date=datetime.today()
        )
        IndividualProfileFactory.create_batch(
            5,
            birth_date=datetime.today() + timedelta(days=1)
        )
        create_birthday_wish_email()
        for birthday_profile in birthday_profiles:
            self.assertIn(
                birthday_profile.user.email,
                Notification.objects.last().recipients
            )
