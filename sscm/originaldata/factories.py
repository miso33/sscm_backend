from datetime import date, timedelta, datetime

import factory
from django.contrib.auth import get_user_model

from sscm.parishes.factories import ParishFactory
from .models import OriginalMember

UserModel = get_user_model()


class OriginalMemberFactory(factory.django.DjangoModelFactory):
    farnost_id = factory.SubFactory(
        ParishFactory,
    )
    firstname = factory.Sequence(lambda n: f"Firstname {n + 1}")
    surname = factory.Sequence(lambda n: f"Surname {n + 1}")
    titul = factory.Sequence(lambda n: f"titul {n + 1}")
    titul2 = factory.Sequence(lambda n: f"titul2 {n + 1}")
    cl_cislo = factory.Sequence(lambda n: n + 1)
    druh_clenstva = "R"
    datum_nar = factory.Sequence(
        lambda n: date.strftime(date.today() - timedelta(weeks=52 * (20 + n)), "%Y-%m-%d")
    )
    povolanie = factory.Sequence(lambda n: f"Proffesion {n + 1}")
    adresa = factory.Sequence(lambda n: f"Address {n + 1}")
    psc = factory.Sequence(lambda n: f"Zip {n + 1}")
    obec = factory.Sequence(lambda n: f"City {n + 1}")
    datum_vstupu = factory.Sequence(
        lambda n: date.today() - timedelta(weeks=52 * (1 + n))
    )
    status = "A"
    poznamka = factory.Sequence(lambda n: f"Note {n + 1}")

    class Meta:
        model = OriginalMember
