import factory
from .DeanshipFactory import DeanshipFactory
from ..models import Parish


class ParishFactory(factory.django.DjangoModelFactory):
    deanship = factory.SubFactory(
        DeanshipFactory,
    )
    name = factory.Sequence(lambda n: 'Name {0}'.format(n + 1))
    status = 'active'

    class Meta:
        model = Parish
