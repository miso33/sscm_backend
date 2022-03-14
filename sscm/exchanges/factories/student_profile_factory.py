from datetime import datetime
from datetime import timedelta, date

import factory

from .school_factory import SchoolFactory
from ..models import StudentProfile
from ...parishes.factories import ParishFactory
from ...users.factories import UserFactory


class StudentProfileFactory(factory.django.DjangoModelFactory):
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

    home_school = factory.SubFactory(SchoolFactory)
    foreign_school = factory.SubFactory(SchoolFactory)
    first_name = factory.Sequence(lambda n: f'first_name {n + 1}')
    last_name = factory.Sequence(lambda n: f'last_name {n + 1}')
    birth_date = factory.Sequence(lambda n: date.today() - timedelta(days=n + 1))
    home_country = "SK"
    residence_country = "DE"
    academic_year = factory.Sequence(lambda n: n + 1)
    semester = StudentProfile.Semester.WINTER
    start = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 1))
    end = factory.Sequence(lambda n: datetime.today() - timedelta(days=n + 1))
    phone_number = factory.Sequence(lambda n: f'+421949{n + 1}')
    university_name = factory.Sequence(lambda n: f'university_name {n + 1}')
    study_filed = factory.Sequence(lambda n: f'study_filed {n + 1}')
    profession = factory.Sequence(lambda n: f'profession {n + 1}')
    language = [{}]
    university_country = "DE"
    member_type = "EXCHANGE"

    class Meta:
        model = StudentProfile
