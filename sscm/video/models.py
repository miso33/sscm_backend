from django.db import models

from sscm.core.models import BaseModel


class Video(BaseModel):
    code = models.CharField(max_length=500, verbose_name="Kód videa")

    class Meta:
        ordering = ["-created"]
        default_related_name = "group_profile"
        verbose_name = "Film"
        verbose_name_plural = "Filmy"

    def __str__(self):
        return f"{self.code}"
