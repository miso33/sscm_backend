from django.db import models
from filer.fields.file import FilerFileField

from sscm.core.models import BaseModel


class Document(BaseModel):
    document = FilerFileField(verbose_name="Dokument", on_delete=models.CASCADE)

    class Meta:
        ordering = ['document']
        default_related_name = 'documents'
        verbose_name = 'Dokument'
        verbose_name_plural = 'Dokumenty'

    def __str__(self):
        return f'{self.document}'
