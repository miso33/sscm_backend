import factory

from ..models import Deanship


class DeanshipFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Name {}'.format(n + 1))
    short = factory.Sequence(lambda n: 'S{}'.format(n + 1))
    status = 'active'

    class Meta:
        model = Deanship
