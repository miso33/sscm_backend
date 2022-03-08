import pytest
from django.urls import reverse
from rest_framework import status

from sscm.parishes.factories import ParishFactory
from sscm.profiles.factories import GroupProfileFactory, IndividualProfileFactory
from sscm.users.tests.base import UserAPITestCase
from ..factories import UserFactory
from ...notifications.models import Notification


class UserRegistrationAPITestCase(UserAPITestCase):

    @pytest.mark.registration
    @pytest.mark.notification
    @pytest.mark.registration_notification
    def test_email_to_admin_after_individual_registration(self):
        password = UserFactory.build().password
        individual_profile = IndividualProfileFactory.build()
        email = UserFactory.build().email
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": email,
                "password1": password,
                "password2": password,
                "profile": {
                    "first_name": individual_profile.first_name,
                    "last_name": individual_profile.last_name,
                    "birth_date": individual_profile.birth_date,
                    "profession": individual_profile.profession,
                    "title_prefix": individual_profile.title_prefix,
                    "title_suffix": individual_profile.title_suffix,
                    "parish": ParishFactory().id,
                    "city": individual_profile.city,
                    "address": individual_profile.address,
                    "zip": individual_profile.zip,
                    "exists": False,
                    "note": individual_profile.note,
                    "member_type": "BASIC",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(
            email,
            Notification.objects.last().body
        )

    @pytest.mark.registration
    @pytest.mark.notification
    @pytest.mark.registration_notification
    def test_email_to_admin_after_group_registration(self):
        password = UserFactory.build().password
        email = UserFactory.build().email
        group_profile = GroupProfileFactory.build()
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": email,
                "password1": password,
                "password2": password,
                "profile": {
                    "name": group_profile.name,
                    "parish": ParishFactory().id,
                    "city": group_profile.city,
                    "address": group_profile.address,
                    "zip": group_profile.zip,
                    "exists": False,
                    "note": group_profile.note,
                    "member_type": "GROUP",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(
            email,
            Notification.objects.last().body
        )
