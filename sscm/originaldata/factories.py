from datetime import date, timedelta

import factory
from django.contrib.auth import get_user_model

from sscm.parishes.factories import ParishFactory
from .models import OriginalMember

UserModel = get_user_model()


class OriginalMemberFactory(factory.django.DjangoModelFactory):
    farnost_id = factory.SubFactory(
        ParishFactory,
    )
    firstname = factory.Sequence(lambda n: 'Firstname {0}'.format(n + 1))
    surname = factory.Sequence(lambda n: 'Surname {0}'.format(n + 1))
    titul = factory.Sequence(lambda n: 'titul {0}'.format(n + 1))
    titul2 = factory.Sequence(lambda n: 'titul2 {0}'.format(n + 1))
    cl_cislo = factory.Sequence(lambda n: n + 1)
    druh_clenstva = "R"
    datum_nar = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 * (20 + n)))
    povolanie = factory.Sequence(lambda n: 'Proffesion {0}'.format(n + 1))
    adresa = factory.Sequence(lambda n: 'Address {0}'.format(n + 1))
    psc = factory.Sequence(lambda n: 'Zip {0}'.format(n + 1))
    obec = factory.Sequence(lambda n: 'City {0}'.format(n + 1))
    datum_vstupu = factory.Sequence(lambda n: date.today() - timedelta(weeks=52 * (1 + n)))
    status = "A"
    poznamka = factory.Sequence(lambda n: 'Note {0}'.format(n + 1))

    class Meta:
        model = OriginalMember
