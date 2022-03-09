from django.db import models

from sscm.core.models import BaseModel


class Parish(BaseModel):
    deanship = models.ForeignKey("parishes.Deanship", on_delete=models.RESTRICT, verbose_name="Dekanát")
    name = models.CharField(max_length=100, verbose_name="Názov")

    class Meta:
        ordering = ["name"]
        default_related_name = "parish"
        verbose_name = "Farnosť"
        verbose_name_plural = "Farnosti"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)
