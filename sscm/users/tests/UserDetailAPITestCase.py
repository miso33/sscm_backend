from django.urls import reverse
from rest_framework import status

from sscm.profiles.factories import GroupProfileFactory, IndividualProfileFactory
from sscm.users.tests.base import UserAPITestCase
from ..factories import UserFactory


class UserDetailAPITestCase(UserAPITestCase):

    def test_group_profile_detail(self):
        user = UserFactory()
        GroupProfileFactory(user=user)
        self.client.force_authenticate(
            user=user
        )
        response = self.client.get(
            path=reverse('rest_user_details'),

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json()['profile'])
        self.assertIn("name", response.json()['profile'])
        self.assertNotIn("last_name", response.json()['profile'])

    def test_individual_profile_detail(self):
        user = UserFactory()
        IndividualProfileFactory(user=user)
        self.client.force_authenticate(
            user=user
        )
        response = self.client.get(
            path=reverse('rest_user_details'),

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json()['profile'])
        self.assertIn("last_name", response.json()['profile'])
        self.assertNotIn("name", response.json()['profile'])

    def test_profile_parish_detail(self):
        user = UserFactory()
        group_profile = GroupProfileFactory(user=user)
        self.client.force_authenticate(
            user=user
        )
        response = self.client.get(
            path=reverse('rest_user_details'),

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(group_profile.parish.name, response.json()['profile']['parish']['name'])
        self.assertEqual(group_profile.parish.id, response.json()['profile']['parish']['id'])
