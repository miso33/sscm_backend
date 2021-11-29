from django.urls import reverse
from rest_framework import status

from sscm.parishes.factories import ParishFactory
from sscm.profiles.factories import GroupProfileFactory, IndividualProfileFactory
from sscm.profiles.models import GroupProfile, IndividualProfile
from sscm.users.tests.base import UserAPITestCase, User
from ..factories import UserFactory


class UserRegistrationUniqueAPITestCase(UserAPITestCase):
    def test_new_group_profile(self):
        password = UserFactory.build().password
        group_profile = GroupProfileFactory.build()
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": UserFactory.build().email,
                "password1": password,
                "password2": password,
                "profile": {
                    "name": group_profile.name,
                    "parish": ParishFactory().id,
                    "city": group_profile.city,
                    "address": group_profile.address,
                    "zip": group_profile.zip,
                    "exists": False,
                    "member_type": "GROUP",
                },
            },
        )

        self.assertEqual(response.json()['user']['profile']['member_type'], "GROUP")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(GroupProfile.objects.filter(name=group_profile.name).exists())

    def test_new_group_profile_wo_user_email(self):
        password = UserFactory.build().password
        group_profile = GroupProfileFactory.build()
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "password1": password,
                "password2": password,
                "profile": {
                    "name": group_profile.name,
                    "parish": ParishFactory().id,
                    "city": group_profile.city,
                    "address": group_profile.address,
                    "zip": group_profile.zip,
                    "exists": False,
                    "member_type": "GROUP",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.json())
        self.assertFalse(GroupProfile.objects.filter(name=group_profile.name).exists())

    def test_new_group_profile_wo_group_name(self):
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
                    "parish": ParishFactory().id,
                    "city": group_profile.city,
                    "address": group_profile.address,
                    "zip": group_profile.zip,
                    "exists": False,
                    "member_type": "GROUP",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.json())
        self.assertFalse(User.objects.filter(email=email).exists())

    def test_new_individual_profile(self):
        password = UserFactory.build().password
        individual_profile = IndividualProfileFactory.build()
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": UserFactory.build().email,
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
                    "member_type": "BASIC",
                },
            },
        )
        self.assertEqual(response.json()['user']['profile']['member_type'], "BASIC")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            IndividualProfile.objects.filter(
                first_name=individual_profile.first_name,
                last_name=individual_profile.last_name,
                birth_date=individual_profile.birth_date,
            ).exists()
        )
