from django.db import models

from sscm.core.models import BaseModel


class Deanship(BaseModel):
    name = models.CharField(max_length=1000)
    short = models.CharField(max_length=5)
    diocese = models.CharField(max_length=5)

    class Meta:
        ordering = ["name"]
        default_related_name = "deanship"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name
