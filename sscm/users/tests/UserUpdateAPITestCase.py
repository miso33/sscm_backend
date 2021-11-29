from django.urls import reverse
from rest_framework import status

from sscm.profiles.factories import GroupProfileFactory, IndividualProfileFactory
from sscm.users.tests.base import UserAPITestCase
from ..factories import UserFactory


class UserUpdateAPITestCase(UserAPITestCase):

    def test_group_profile_update(self):
        user = UserFactory()
        original_group_profile = GroupProfileFactory(user=user)
        new_group_profile = GroupProfileFactory.build()
        self.assertNotEqual(original_group_profile.name, new_group_profile.name)
        self.client.force_authenticate(
            user=user
        )
        response = self.client.put(
            path=reverse('rest_user_details'),
            data={
                "email": user.email,
                "profile": {
                    "name": new_group_profile.name,
                    "parish": original_group_profile.parish.id,
                    "city": original_group_profile.city,
                    "address": original_group_profile.address,
                    "zip": original_group_profile.zip,
                    "member_type": "GROUP"
                }
            }

        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['profile']['name'], new_group_profile.name)

    def test_individual_profile_update(self):
        user = UserFactory()
        original_individual_profile = IndividualProfileFactory(user=user)
        individual_profile = IndividualProfileFactory.build()
        self.assertNotEqual(original_individual_profile.last_name, individual_profile.last_name)
        self.client.force_authenticate(
            user=user
        )
        response = self.client.patch(
            path=reverse('rest_user_details'),
            data={
                "email": user.email,
                "profile": {
                    "last_name": individual_profile.last_name,
                    "first_name": original_individual_profile.first_name,
                    "birth_date": original_individual_profile.birth_date,
                    "profession": original_individual_profile.profession,
                    "title_prefix": original_individual_profile.title_prefix,
                    "title_suffix": original_individual_profile.title_suffix,
                    "parish": original_individual_profile.parish.id,
                    "city": original_individual_profile.city,
                    "address": original_individual_profile.address,
                    "zip": original_individual_profile.zip,
                    "member_type": "GROUP"
                }
            }

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['profile']['last_name'], individual_profile.last_name)
