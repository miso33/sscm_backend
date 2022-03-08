from datetime import datetime, timedelta
from django_countries import countries
import factory

from ..models import School


class SchoolFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'name {n + 1}')
    address = factory.Sequence(lambda n: f'address {n + 1}')
    city = factory.Sequence(lambda n: f'city {n + 1}')
    country = "SK"
    cooperation_start = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 120))
    first_name = factory.Sequence(lambda n: f'first_name {n + 1}')
    last_name = factory.Sequence(lambda n: f'last_name {n + 1}')
    phone_number = factory.Sequence(lambda n: f'+421949{n+1}')
    email = factory.Sequence(lambda n: f'email@emal{n + 1}.com')

    class Meta:
        model = School
