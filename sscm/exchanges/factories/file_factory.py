import factory
from django.core.files.base import ContentFile

from filer.models.filemodels import File


class FileFactory(factory.django.DjangoModelFactory):
    file = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
            "baner.jpg",
        )
    )

    class Meta:
        model = File
