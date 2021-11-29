from django.db import models

from sscm.core.models import BaseModel


class MemberProfile(BaseModel):
    class MemberType(models.TextChoices):
        BASIC = "BASIC", "Riadny"
        GROUP = "GROUP", "Skupinový"
        FOUNDER = "FOUNDER", "Zakladajúci"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Aktívny"
        INACTIVE = "INACTIVE", "Neaktívny"
        OUTAGE = "OUTAGE", "Vyradený"
        DECEASED = "DECEASED", "Zosnulý"

    parish = models.ForeignKey("parishes.Parish", on_delete=models.RESTRICT, verbose_name="Farnosť")
    member_number = models.IntegerField(null=True, blank=True, verbose_name="Členské číslo")
    city = models.CharField(max_length=1000, blank=True, verbose_name="Obec")
    address = models.CharField(max_length=1000, blank=True, verbose_name="Adresa")
    zip = models.CharField(max_length=100, blank=True, verbose_name="PSČ")
    enter_date = models.DateField(null=True, blank=True, verbose_name="Dátum vstupu")
    note = models.CharField(max_length=5000, blank=True, verbose_name="Poznámka")
    member_type = models.CharField(
        max_length=10,
        choices=MemberType.choices,
        default=MemberType.BASIC,
        verbose_name="Druh členstva"
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.INACTIVE,
        verbose_name="Status"
    )

    class Meta:
        ordering = ['member_number']
        default_related_name = 'member'
        verbose_name = "Člen"
        verbose_name_plural = "Členovia"
        indexes = [
            models.Index(fields=['member_number']),
        ]

    def __str__(self):
        return self.member_number
