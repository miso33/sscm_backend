from django.contrib.auth import get_user_model
from django.urls import include, path

from sscm.core.tests import BaseAPITestCase

User = get_user_model()


class UserAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("account/registration/", include("dj_rest_auth.registration.urls")),
        path("account/", include("dj_rest_auth.urls")),
    ]
