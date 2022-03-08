from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.db import models

from sscm.core.models import BaseModel


class Notification(BaseModel):
    class Channel(models.TextChoices):
        EMIAL = "EMAIL"
        FIREBASE = "FIREBASE"

    recipients = ArrayField(models.CharField(max_length=200))
    recipients_copy = ArrayField(
        models.CharField(max_length=200), blank=True, null=True
    )
    recipients_blind_copy = ArrayField(
        models.CharField(max_length=200), blank=True, null=True
    )
    subject = models.CharField(max_length=1000, blank=True)
    body = RichTextField(max_length=1000, blank=True)
    body_raw = models.CharField(max_length=1000, blank=True)
    data = models.JSONField(null=True)
    attachment_file = models.FileField(null=True)
    send_schedule = models.DateTimeField(auto_now_add=True)
    attempts_max = models.PositiveSmallIntegerField(default=10)
    attempts_number = models.PositiveSmallIntegerField(default=0)
    last_attempt = models.DateTimeField(null=True)
    sent_datetime = models.DateTimeField(null=True)
    sent = models.BooleanField(default=False)
    channel = models.CharField(
        choices=Channel.choices,
        default=Channel.EMIAL,
        max_length=20
    )

    class Meta:
        ordering = ["created"]
        default_related_name = "emails"
        indexes = [
            models.Index(fields=["-created"]),
            models.Index(fields=["sent"]),
        ]

    def __str__(self):
        return f"{self.recipients}"
