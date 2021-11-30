from datetime import date, timedelta

import factory

from sscm.parishes.factories import ParishFactory
from sscm.users.factories import UserFactory
from ..models import IndividualProfile


class IndividualProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(
        UserFactory,
    )
    parish = factory.SubFactory(
        ParishFactory,
    )
    member_number = factory.Sequence(lambda n: n + 1)
    city = factory.Sequence(lambda n: f"City {n + 1}")
    address = factory.Sequence(lambda n: f"Address {n + 1}")
    zip = factory.Sequence(lambda n: f"Zip {n + 1}")
    enter_date = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 + n))
    note = factory.Sequence(lambda n: f"Note {n + 1}")
    first_name = factory.Sequence(lambda n: f"First {n + 1}")
    last_name = factory.Sequence(lambda n: f"Last {n + 1}")
    birth_date = factory.Sequence(lambda n: date.today() - timedelta(days=n + 1))
    profession = factory.Sequence(lambda n: f"Profession {n + 1}")
    title_prefix = factory.Sequence(lambda n: f"Title Prefix {n + 1}")
    title_suffix = factory.Sequence(lambda n: f"Title Surfix {n + 1}")

    class Meta:
        model = IndividualProfile
