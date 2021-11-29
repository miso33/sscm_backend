from django.contrib.auth.models import AbstractUser

from sscm.profiles.services import ReadProfileService


class User(AbstractUser):
    @property
    def profile(self):
        return ReadProfileService().get_serializer(self)
