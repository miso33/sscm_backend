import factory
from django.urls import reverse
from rest_framework import status

from sscm.users.tests.base import UserAPITestCase
from ..factories import UserFactory


class UserLoginAPITestCase(UserAPITestCase):

    def test_login(self):
        password = UserFactory.build().password
        user = UserFactory(password=factory.PostGenerationMethodCall('set_password', password))
        response = self.client.post(
            path=reverse('rest_login'),
            data={
                "email": user.email,
                "password": password,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
