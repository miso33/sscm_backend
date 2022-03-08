from django.db import models

from sscm.core.models import BaseModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from .base import ExchangeCountries


class School(BaseModel):
    name = models.CharField(max_length=30, verbose_name="Názov")
    address = models.CharField(max_length=500, verbose_name="Adresa")
    city = models.CharField(max_length=500, verbose_name="Mesto")
    country = CountryField(verbose_name="Krajina", countries=ExchangeCountries)
    cooperation_start = models.DateField(null=True, verbose_name="Začiatok spolupráce")
    first_name = models.CharField(max_length=30, blank=True, verbose_name="Krstné meno")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="Priezvisko")
    phone_number = PhoneNumberField(verbose_name="Mobilné číslo", blank=True)
    email = models.EmailField(verbose_name="E-mail", blank=True)

    class Meta:
        ordering = ['name']
        default_related_name = 'schools'
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Škola'
        verbose_name_plural = 'Školy'

    def __str__(self):
        return f'{self.name}'
