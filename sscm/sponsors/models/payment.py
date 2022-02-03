from django.db import models

from sscm.core.models import BaseModel


class Payment(BaseModel):
    class Currency(models.TextChoices):
        EUR = "EUR", "Euro"
        USD = "USD", "Dolár"

    class Method(models.TextChoices):
        CASH = "CASH", "Hotovosť"
        TRANSFER = "TRANSFER", "Prevod na účet"

    sponsor = models.ForeignKey(
        "Sponsor",
        on_delete=models.CASCADE,
        verbose_name="Sponzor"
    )
    date = models.DateField(verbose_name="Dátum")
    sum = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Suma")
    note = models.CharField(max_length=500, verbose_name="Poznámka")
    currency = models.CharField(
        choices=Currency.choices,
        default=Currency.EUR,
        max_length=20,
        verbose_name="Mena"
    )
    method = models.CharField(
        choices=Method.choices,
        default=Method.CASH,
        max_length=20,
        verbose_name="Platobná metóda"
    )

    class Meta:
        ordering = ['-created']
        default_related_name = 'payments'
        indexes = [
            models.Index(fields=['sponsor']),
            models.Index(fields=['currency']),
            models.Index(fields=['method']),
        ]
        verbose_name = 'Platba'
        verbose_name_plural = 'Platby'

    def __str__(self):
        return f'{self.sponsor.first_name} {self.sponsor.last_name} {self.date}'
