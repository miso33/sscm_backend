from datetime import datetime, timedelta

import factory

from .school_factory import SchoolFactory
from ..models import Student


class StudentFactory(factory.django.DjangoModelFactory):
    home_school = factory.SubFactory(SchoolFactory)
    foreign_school = factory.SubFactory(SchoolFactory)
    first_name = factory.Sequence(lambda n: f'first_name {n + 1}')
    last_name = factory.Sequence(lambda n: f'last_name {n + 1}')
    birth_date = factory.Sequence(lambda n: f'birth_date {n + 1}')
    address = factory.Sequence(lambda n: f'address {n + 1}')
    home_country = "SK"
    residence_country = "DE"
    academic_year = factory.Sequence(lambda n: n + 1)
    semester = Student.Semester.WINTER
    start = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 1))
    end = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 1))
    phone_number = factory.Sequence(lambda n: f'+421949{n + 1}')
    university_name = factory.Sequence(lambda n: f'university_name {n + 1}')
    study_filed = factory.Sequence(lambda n: f'study_filed {n + 1}')
    profession = factory.Sequence(lambda n: f'profession {n + 1}')
    language = [{}]
    university_country = "DE"

    class Meta:
        model = Student
