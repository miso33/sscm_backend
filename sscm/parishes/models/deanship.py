from django.db import models

from sscm.core.models import BaseModel


class Deanship(BaseModel):
    name = models.CharField(max_length=1000, verbose_name="Názov")
    short = models.CharField(max_length=5, verbose_name="Skratka")
    diocese = models.CharField(max_length=5, verbose_name="Diecéza")

    class Meta:
        ordering = ["name"]
        default_related_name = "deanship"
        verbose_name = "Dekanát"
        verbose_name_plural = "Dekanáty"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)
