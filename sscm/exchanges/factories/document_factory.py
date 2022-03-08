import factory

from .file_factory import FileFactory
from ..models import Document


class DocumentFactory(factory.django.DjangoModelFactory):
    document = factory.SubFactory(
        FileFactory
    )

    class Meta:
        model = Document
