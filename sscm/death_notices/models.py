from django.conf import settings
from django.db import models

from sscm.core.models import BaseModel


class DeathNotice(BaseModel):
    sender = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Užívateľ",
    )
    first_name = models.CharField(
        max_length=100, verbose_name="Krstné meno"
    )
    last_name = models.CharField(max_length=100, verbose_name="Priezvisko")
    birth_date = models.DateField(verbose_name="Dátum narodenia")

    class Meta:
        ordering = ["last_name"]
        default_related_name = "death_notice"
        verbose_name = "Nahlásene úmrtie"
        verbose_name_plural = "Nahlásene úmrtia"
        indexes = [
            models.Index(fields=["first_name"]),
            models.Index(fields=["last_name"]),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
