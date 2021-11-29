import factory
from .deanship_factory import DeanshipFactory
from ..models import Parish


class ParishFactory(factory.django.DjangoModelFactory):
    deanship = factory.SubFactory(
        DeanshipFactory,
    )
    name = factory.Sequence(lambda n: f"Name {n + 1}")
    status = "active"

    class Meta:
        model = Parish
