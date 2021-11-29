from django.db import models

from sscm.core.models import BaseModel


class OriginalMember(BaseModel):
    firstname = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    titul = models.CharField(max_length=50, blank=True)
    titul2 = models.CharField(max_length=50, blank=True)
    cl_cislo = models.IntegerField()
    druh_clenstva = models.CharField(max_length=50, blank=True)
    datum_nar = models.DateField(null=True)
    povolanie = models.CharField(max_length=100, blank=True)
    adresa = models.CharField(max_length=500, blank=True)
    psc = models.CharField(max_length=100, blank=True)
    obec = models.CharField(max_length=100, blank=True)
    farnost_id = models.ForeignKey("parishes.Parish", on_delete=models.RESTRICT)
    datum_vstupu = models.DateField(null=True)
    status = models.CharField(max_length=100, blank=True)
    poznamka = models.CharField(max_length=1000, blank=True)

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
