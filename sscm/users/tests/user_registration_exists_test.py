from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from sscm.originaldata.factories import OriginalMemberFactory
from sscm.users.tests.base import UserAPITestCase
from ..factories import UserFactory
from ...profiles.models import GroupProfile, IndividualProfile

UserModel = get_user_model()


class UserRegistrationExistsAPITestCase(UserAPITestCase):
    def test_exists_group_profile(self):
        password = UserFactory.build().password
        surname = OriginalMemberFactory.build().surname
        OriginalMemberFactory(
            firstname="x", druh_clenstva="Z", status="Z", surname=surname.capitalize()
        )
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": UserFactory.build().email,
                "password1": password,
                "password2": password,
                "profile": {
                    "name": surname,
                    "exists": True,
                    "member_type": "GROUP",
                },
            },
        )
        group_profile = GroupProfile.objects.filter(name=surname)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(group_profile.exists())
        self.assertEqual(group_profile.get().member_type, "FOUNDER")
        self.assertEqual(group_profile.get().status, "DECEASED")

    def test_exists_individual_profile(self):
        password = UserFactory.build().password
        original_member = OriginalMemberFactory(druh_clenstva="Z", status="Z")
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": UserFactory.build().email,
                "password1": password,
                "password2": password,
                "profile": {
                    "first_name": original_member.firstname,
                    "last_name": original_member.surname,
                    "birth_date": original_member.datum_nar,
                    "exists": True,
                    "member_type": "BASIC",
                },
            },
        )
        individual_profile = IndividualProfile.objects.filter(
            last_name=original_member.surname
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(individual_profile.exists())
        self.assertEqual(individual_profile.get().member_type, "FOUNDER")
        self.assertEqual(individual_profile.get().status, "DECEASED")

    def test_exists_not_found_group_profile(self):
        password = UserFactory.build().password
        email = UserFactory.build().email
        surname = OriginalMemberFactory.build().surname
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": email,
                "password1": password,
                "password2": password,
                "profile": {
                    "name": surname,
                    "exists": True,
                    "member_type": "GROUP",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(GroupProfile.objects.filter(name=surname))
        self.assertFalse(UserModel.objects.filter(email=email))

    def test_exists_individual_not_found_profile(self):
        password = UserFactory.build().password
        email = UserFactory.build().email
        surname = OriginalMemberFactory.build().surname
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": UserFactory.build().email,
                "password1": password,
                "password2": password,
                "profile": {
                    "first_name": OriginalMemberFactory.build().firstname,
                    "last_name": surname,
                    "birth_date": OriginalMemberFactory.build().datum_nar,
                    "exists": True,
                    "member_type": "BASIC",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(IndividualProfile.objects.filter(last_name=surname))
        self.assertFalse(UserModel.objects.filter(email=email))

    def test_exists_group_profile_empty_note(self):
        password = UserFactory.build().password
        surname = OriginalMemberFactory.build().surname
        OriginalMemberFactory(
            firstname="x",
            druh_clenstva="Z",
            status="Z",
            surname=surname.capitalize(),
            poznamka="",
        )
        response = self.client.post(
            path=reverse("rest_register"),
            data={
                "email": UserFactory.build().email,
                "password1": password,
                "password2": password,
                "profile": {
                    "name": surname,
                    "exists": True,
                    "member_type": "GROUP",
                },
            },
        )
        group_profile = GroupProfile.objects.filter(name=surname)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(group_profile.exists())
        self.assertEqual(group_profile.get().member_type, "FOUNDER")
        self.assertEqual(group_profile.get().status, "DECEASED")
