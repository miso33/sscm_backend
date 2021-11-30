import factory

from .models import Video


class VideoFactory(factory.django.DjangoModelFactory):
    code = factory.Sequence(lambda n: f"Code{n + 1}")
    status = "active"

    class Meta:
        model = Video
