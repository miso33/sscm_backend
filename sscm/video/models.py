from django.db import models

from sscm.core.models import BaseModel


class Video(BaseModel):
    code = models.CharField(max_length=500)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.code}"
