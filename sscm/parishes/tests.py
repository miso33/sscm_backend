from django.urls import include, path
from django.urls import reverse
from rest_framework import status

from .factories import ParishFactory
from ..core.tests import BaseAPITestCase


class ParishAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("parishes/", include("config.urls")),
    ]

    def test_list(self):
        ParishFactory.create_batch(10)
        response = self.client.get(
            path=reverse("parish-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
