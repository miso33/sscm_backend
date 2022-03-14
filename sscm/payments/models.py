from django.db import models
from django.conf import settings

from sscm.core.models import BaseModel
from sscm.payments.managers import PaymentManager


class Payment(BaseModel):
    class Method(models.TextChoices):
        CASH = "CASH", "Hotovosť"
        TRANSFER = "TRANSFER", "Prevod na účet"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Užívateľské konto",
        null=True,
        blank=True
    )
    date = models.DateField(verbose_name="Dátum")
    sum = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name="Suma",
        null=True,
        blank=True
    )
    method = models.CharField(
        choices=Method.choices,
        default=Method.CASH,
        max_length=20,
        verbose_name="Platobná metóda"
    )
    document_number = models.CharField(max_length=500, verbose_name="Číslo dokladu")
    gift = models.BooleanField(default=False, verbose_name="Členské")
    membership = models.BooleanField(default=False, verbose_name="Dar")
    objects = PaymentManager()

    class Meta:
        ordering = ['-created']
        default_related_name = 'payments'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['date']),
            models.Index(fields=['method']),
        ]
        verbose_name = 'Platba'
        verbose_name_plural = 'Platby'

    def __str__(self):
        return f'{self.user.email}'
