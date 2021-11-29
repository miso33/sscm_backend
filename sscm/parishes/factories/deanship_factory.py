import factory

from ..models import Deanship


class DeanshipFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Name {n + 1}")
    short = factory.Sequence(lambda n: f"S{n + 1}")
    status = "active"

    class Meta:
        model = Deanship
