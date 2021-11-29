from django.db import models

from sscm.core.models import BaseModel


class Parish(BaseModel):
    deanship = models.ForeignKey("parishes.Deanship", on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        default_related_name = "parish"
        verbose_name = "Parish"
        verbose_name_plural = "Parishes"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name
