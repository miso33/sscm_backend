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
    city = factory.Sequence(lambda n: 'City {0}'.format(n + 1))
    address = factory.Sequence(lambda n: 'Address {0}'.format(n + 1))
    zip = factory.Sequence(lambda n: 'Zip {0}'.format(n + 1))
    enter_date = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 + n))
    note = factory.Sequence(lambda n: 'Note {0}'.format(n + 1))
    first_name = factory.Sequence(lambda n: 'First {0}'.format(n + 1))
    last_name = factory.Sequence(lambda n: 'Last {0}'.format(n + 1))
    birth_date = factory.Sequence(lambda n: date.today() - timedelta(days=n + 1))
    profession = factory.Sequence(lambda n: 'Profession {0}'.format(n + 1))
    title_prefix = factory.Sequence(lambda n: 'Title Prefix {0}'.format(n + 1))
    title_suffix = factory.Sequence(lambda n: 'Title Surfix {0}'.format(n + 1))

    class Meta:
        model = IndividualProfile
