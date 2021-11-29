from django.conf import settings
from django.db import models

from .MemberProfile import MemberProfile


class IndividualProfile(MemberProfile):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Užívateľské konto",
    )
    first_name = models.CharField(
        max_length=100, blank=True, verbose_name="Krstné meno"
    )
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Priezvisko")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Dátum narodenia")
    profession = models.CharField(
        max_length=500, blank=True, verbose_name="Zamestnanie"
    )
    title_prefix = models.CharField(
        max_length=50, blank=True, verbose_name="Titul pred menom"
    )
    title_suffix = models.CharField(
        max_length=50, blank=True, verbose_name="Titul za menom"
    )

    class Meta:
        ordering = ["last_name"]
        default_related_name = "individual_profile"
        verbose_name = "Jednotlivec"
        verbose_name_plural = "Jednotlivci"
        indexes = [
            models.Index(fields=["last_name"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
