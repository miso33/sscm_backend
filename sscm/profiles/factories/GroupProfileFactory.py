from datetime import timedelta, date

import factory

from sscm.parishes.factories import ParishFactory
from sscm.users.factories import UserFactory
from ..models import GroupProfile


class GroupProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(
        UserFactory,
    )
    parish = factory.SubFactory(
        ParishFactory,
    )
    name = factory.Sequence(lambda n: 'Name {0}'.format(n + 1))
    member_number = factory.Sequence(lambda n: n + 1)
    city = factory.Sequence(lambda n: 'City {0}'.format(n + 1))
    address = factory.Sequence(lambda n: 'Address {0}'.format(n + 1))
    zip = factory.Sequence(lambda n: 'Zip {0}'.format(n + 1))
    enter_date = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 + n))
    note = factory.Sequence(lambda n: 'Note {0}'.format(n + 1))
    member_type = "GROUP"

    class Meta:
        model = GroupProfile
