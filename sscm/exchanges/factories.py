from datetime import datetime, timedelta

import factory

from .models import School


class StudentFactory(factory.django.DjangoModelFactory):
    home_school = factory.SubFactory(Home_schoolFactory)
    foreign_school = factory.SubFactory(Foreign_schoolFactory)
    first_name = factory.Sequence(lambda n: f'first_name {n + 1}')
    last_name = factory.Sequence(lambda n: f'last_name {n + 1}')
    birth_date = factory.Sequence(lambda n: f'birth_date {n + 1}')
    address = factory.Sequence(lambda n: f'address {n + 1}')
    home_country = factory.Sequence(lambda n: f'home_country {n + 1}')
    residence_country = factory.Sequence(lambda n: f'residence_country {n + 1}')
    academic_year = factory.Sequence(lambda n: n + 1)
    semester = factory.Sequence(lambda n: f'semester {n + 1}')
    start = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 1))
    end = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 1))
    phone_number  = factory.Sequence(lambda n: f'phone_number  {n + 1}')
    university_name = factory.Sequence(lambda n: f'university_name {n + 1}')
    study_filed = factory.Sequence(lambda n: f'study_filed {n + 1}')
    profession = factory.Sequence(lambda n: f'profession {n + 1}')
    language = [{}]
    university_country = factory.Sequence(lambda n: f'university_country {n + 1}')
    status = 'active'

    class Meta:
        model = Student
