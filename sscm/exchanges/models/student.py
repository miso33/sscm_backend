from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from ...core.countries import ExchangeCountries
from ...profiles.models import MemberProfile


class StudentProfile(MemberProfile):
    class Semester(models.TextChoices):
        WINTER = "WINTER", "Zimný"
        SUMMER = "SUMMER", "Letný"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Užívateľské konto",
        related_name="student_profile"
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
    birth_date = models.DateField(max_length=500, verbose_name="Dátum narodenia")
    home_country = CountryField(verbose_name="Domáca krajina", countries=ExchangeCountries)
    residence_country = CountryField(verbose_name="Krajina, do ktorej bol vymenený", countries=ExchangeCountries)
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
    university_name = models.CharField(max_length=500, blank=True, verbose_name="Univerzita, do ktorej bol vymenený")
    university_country = CountryField(blank=True, countries=ExchangeCountries,
                                      verbose_name="Krajina univerzity, do ktorej bol vymenený")
    study_filed = models.CharField(max_length=500, blank=True, verbose_name="Študijný odbor")
    profession = models.CharField(max_length=500, blank=True, verbose_name="Povolanie")
    language = models.JSONField(verbose_name="Jazyky")
    title_prefix = models.CharField(
        max_length=50, blank=True, verbose_name="Titul pred menom"
    )
    title_suffix = models.CharField(
        max_length=50, blank=True, verbose_name="Titul za menom"
    )
    death_date = models.DateField(null=True, blank=True, verbose_name="Dátum úmrtia")

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

    # @property
    # def is_member(self):
    #     return self.member is None
