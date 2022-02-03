from django.db import models

from sscm.core.models import BaseModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from .base import ExchangeCountries


class Student(BaseModel):
    class Semester(models.TextChoices):
        WINTER = "WINTER", "Zimný"
        SUMMER = "SUMMER", "Letný"

    member = models.ForeignKey(
        'profiles.MemberProfile',
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Člen"
    )
    foreign_school = models.ForeignKey(
        'School',
        on_delete=models.CASCADE,
        verbose_name="Zahraničná škola",
        related_name="foreign_students",
    )
    home_school = models.ForeignKey(
        'School',
        on_delete=models.CASCADE,
        verbose_name="Domáca škola",
        related_name="home_students"
    )
    first_name = models.CharField(max_length=50, verbose_name="Krstné meno")
    last_name = models.CharField(max_length=50, verbose_name="Priezvisko")
    birth_date = models.CharField(max_length=500, verbose_name="Dátum narodenia")
    email = models.EmailField(max_length=50, verbose_name="E-mail")
    address = models.CharField(max_length=500, verbose_name="Adresa")
    home_country = CountryField(verbose_name="Domáca krajina", countries=ExchangeCountries)
    residence_country = CountryField(verbose_name="Krajina pobytu", countries=ExchangeCountries)
    academic_year = models.IntegerField(null=True, blank=True, verbose_name="Školský rok pobytu")
    semester = models.CharField(
        choices=Semester.choices,
        default=Semester.WINTER,
        max_length=10,
        verbose_name="Polrok pobytu",
        blank=True
    )
    start = models.DateField(null=True, verbose_name="Dátum začiatku")
    end = models.DateField(null=True, verbose_name="Dátum konca")
    phone_number = PhoneNumberField(verbose_name="Mobilné číslo")
    university_name = models.CharField(max_length=500, blank=True, verbose_name="Univerzita názov")
    university_country = CountryField(blank=True, countries=ExchangeCountries)
    study_filed = models.CharField(max_length=500, blank=True, verbose_name="Študijný odbor")
    profession = models.CharField(max_length=500, blank=True, verbose_name="Povolanie")
    language = models.JSONField(verbose_name="Jazyky")

    class Meta:
        ordering = ['-created']
        default_related_name = 'students'
        indexes = [
            models.Index(fields=['last_name']),
            models.Index(fields=['semester']),
            models.Index(fields=['home_country']),
            models.Index(fields=['residence_country']),
            models.Index(fields=['birth_date']),
        ]
        verbose_name = 'Študent'
        verbose_name_plural = 'Študenti'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
