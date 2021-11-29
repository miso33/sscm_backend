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
    city = factory.Sequence(lambda n: f"City {n + 1}")
    address = factory.Sequence(lambda n: f"Address {n + 1}")
    zip = factory.Sequence(lambda n: f"Zip {n + 1}")
    enter_date = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 + n))
    note = factory.Sequence(lambda n: f"Note {n + 1}")

    class Meta:
        model = MemberProfile
