from datetime import timedelta, date

import factory
from django.contrib.auth import get_user_model

from sscm.parishes.factories import ParishFactory
from ..models import MemberProfile

UserModel = get_user_model()


class MemberProfileFactory(factory.django.DjangoModelFactory):
    parish = factory.SubFactory(
        ParishFactory,
    )
    member_number = factory.Sequence(lambda n: n + 1)
    city = factory.Sequence(lambda n: 'City {0}'.format(n + 1))
    address = factory.Sequence(lambda n: 'Address {0}'.format(n + 1))
    zip = factory.Sequence(lambda n: 'Zip {0}'.format(n + 1))
    enter_date = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 + n))
    note = factory.Sequence(lambda n: 'Zip {0}'.format(n + 1))

    class Meta:
        model = MemberProfile
