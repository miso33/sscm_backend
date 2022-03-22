from django.db import models

from sscm.core.models import BaseModel


class OriginalMember(BaseModel):
    member = models.OneToOneField(
        'profiles.MemberProfile',
        on_delete=models.CASCADE,
        verbose_name="Člen",
        null=True,
        blank=True
    )
    firstname = models.CharField(max_length=100, blank=True, verbose_name="Krstné meno")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Priezvisko")
    titul = models.CharField(max_length=50, blank=True, verbose_name="Titul pred menom")
    titul2 = models.CharField(max_length=50, blank=True, verbose_name="Titul za menom")
    cl_cislo = models.IntegerField(verbose_name="Členské číslo")
    druh_clenstva = models.CharField(max_length=50, blank=True, verbose_name="Druh členstva")
    datum_nar = models.DateField(null=True, verbose_name="Dátum narodenia")
    povolanie = models.CharField(max_length=100, blank=True, verbose_name="Povolanie")
    adresa = models.CharField(max_length=500, blank=True, verbose_name="Adresa")
    psc = models.CharField(max_length=100, blank=True, verbose_name="PSČ")
    obec = models.CharField(max_length=100, blank=True, verbose_name="Obec")
    farnost_id = models.ForeignKey("parishes.Parish", on_delete=models.RESTRICT, verbose_name="Farnosť")
    datum_vstupu = models.DateField(null=True, verbose_name="Dátum výstupu")
    status = models.CharField(max_length=100, blank=True, verbose_name="Status")
    poznamka = models.CharField(max_length=1000, blank=True, verbose_name="Poznámka")
    leave_date = models.DateField(null=True, blank=True, verbose_name="Dátum vyradenia")
    death_date = models.DateField(null=True, blank=True, verbose_name="Dátum úmrtia")
    email = models.CharField(max_length=100, blank=True, verbose_name="E-mail")

    class Meta:
        ordering = ["surname"]
        default_related_name = "original_member"
        verbose_name = "Pôvodné údaje členov"
        verbose_name_plural = "Pôvodné údaje členov"
        indexes = [
            models.Index(fields=["surname"]),
        ]

    def __str__(self):
        return f"{self.firstname} {self.surname}"
