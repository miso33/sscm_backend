from django.urls import include, path
from django.urls import reverse
from rest_framework import status

from .factories import ParishFactory, DeathNoticeFactory
from ..core.tests import BaseAPITestCase
from ..users.factories import UserFactory


class DeathNoticeFactoryAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("death_note/", include("config.urls")),
    ]

    def test_create(self):
        self.login_with_all_permissions(user=UserFactory())
        death_notice = DeathNoticeFactory.build()
        response = self.client.post(
            path=reverse("death-note-create"),
            data={
                "last_name": death_notice.last_name,
                "first_name": death_notice.first_name,
                "birth_date": death_notice.birth_date,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
