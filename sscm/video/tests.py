from django.urls import include, path
from django.urls import reverse
from rest_framework import status

from .factories import VideoFactory
from ..core.tests import BaseAPITestCase
from ..profiles.factories import IndividualProfileFactory
from ..profiles.models import MemberProfile
from ..users.factories import UserFactory


class VideoAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("video/", include("config.urls")),
    ]

    def test_get_code_authenticated_user(self):
        video = VideoFactory()
        user = UserFactory()
        IndividualProfileFactory(user=user, status=MemberProfile.Status.ACTIVE)
        self.client.force_authenticate(user=user)
        response = self.client.get(
            path=reverse("get_code"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["code"], video.code)

    def test_get_code_unauthenticated_user(self):
        VideoFactory()
        response = self.client.get(
            path=reverse("get_code"),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_code_no_video(self):
        user = UserFactory()
        IndividualProfileFactory(user=user, status=MemberProfile.Status.ACTIVE)
        self.client.force_authenticate(user=user)
        response = self.client.get(
            path=reverse("get_code"),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_code_inactive_profile(self):
        VideoFactory()
        user = UserFactory()
        IndividualProfileFactory(user=user, status=MemberProfile.Status.INACTIVE)
        self.client.force_authenticate(user=user)
        response = self.client.get(
            path=reverse("get_code"),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_code_no_profile(self):
        VideoFactory()
        user = UserFactory()
        self.client.force_authenticate(user=user)
        response = self.client.get(
            path=reverse("get_code"),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
