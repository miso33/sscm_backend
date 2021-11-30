from django.conf import settings
from django.db import models

from .member_profile import MemberProfile


class GroupProfile(MemberProfile):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Užívateľské konto",
    )
    name = models.CharField(max_length=100, unique=True, verbose_name="Názov")

    class Meta:
        ordering = ["name"]
        default_related_name = "group_profile"
        verbose_name = "Skupina"
        verbose_name_plural = "Skupiny"

        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)
