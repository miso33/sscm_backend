from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from sscm.core.countries import SponsorCountries
from sscm.core.models import BaseModel


class Sponsor(BaseModel):
    class Language(models.TextChoices):
        SK = "SK,", "Slovenčina"
        DE = "DE", "Nemčina"
        EN = "EN", "Angličtina"

    name = models.CharField(max_length=30, verbose_name="Názov")
    birth_date = models.DateField(verbose_name="Dátum narodenia", blank=True, null=True)
    address = models.CharField(max_length=500, verbose_name="Adresa", blank=True)
    city = models.CharField(max_length=500, verbose_name="Mesto", blank=True)
    country = CountryField(verbose_name="Krajina", countries=SponsorCountries)
    email = models.CharField(max_length=500, verbose_name="E-mail")
    phone_number = PhoneNumberField(max_length=500, verbose_name="Telefónne číslo")
    profession = models.CharField(max_length=500, verbose_name="Povolanie")
    account_number = models.CharField(max_length=500, blank=True, verbose_name="Číslo účtu")
    language = models.CharField(
        choices=Language.choices,
        default=Language.SK,
        max_length=20,
        verbose_name="Jazyk"
    )

    class Meta:
        ordering = ['name']
        default_related_name = 'sponsors'
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Sponzor'
        verbose_name_plural = 'Sponzori'

    def __str__(self):
        return f'{self.name}'
