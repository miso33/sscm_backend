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
    name = factory.Sequence(lambda n: f"Name {n + 1}")
    member_number = factory.Sequence(lambda n: n + 1)
    city = factory.Sequence(lambda n: f"City {n + 1}")
    address = factory.Sequence(lambda n: f"Address {n + 1}")
    zip = factory.Sequence(lambda n: f"Zip {n + 1}")
    enter_date = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 + n))
    note = factory.Sequence(lambda n: f"Note {n + 1}")
    member_type = "GROUP"

    class Meta:
        model = GroupProfile
