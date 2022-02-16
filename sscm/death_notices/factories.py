from datetime import date, timedelta

import factory

from sscm.users.factories import UserFactory
from .models import DeathNotice


class DeathNoticeFactory(factory.django.DjangoModelFactory):
    sender = factory.SubFactory(
        UserFactory,
    )
    first_name = factory.Sequence(lambda n: f"First {n + 1}")
    last_name = factory.Sequence(lambda n: f"Last {n + 1}")
    birth_date = factory.Sequence(lambda n: date.today() - timedelta(days=n + 1))

    class Meta:
        model = DeathNotice
