import pytest
from django.urls import include, path
from django.urls import reverse
from rest_framework import status

from .factories import StudentFactory, SchoolFactory
from .models import Student
from ..core.tests import BaseAPITestCase
from ..users.factories import UserFactory


class StudentAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("student/", include("config.urls")),
    ]

    @pytest.mark.student
    def test_list(self):
        self.login_with_all_permissions(user=UserFactory())
        StudentFactory.create_batch(10)
        response = self.client.get(
            path=reverse("student-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.json()['results']),
            Student.objects.count()
        )

    @pytest.mark.student
    def test_list_school_name(self):
        self.login_with_all_permissions(user=UserFactory())
        home_school = SchoolFactory()
        foreign_school = SchoolFactory()
        StudentFactory(
            home_school=home_school,
            foreign_school=foreign_school,
        )
        response = self.client.get(
            path=reverse("student-list"),
        )
        student_response = response.json()['results'][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(student_response['home_school'], home_school.name)
        self.assertEqual(student_response['foreign_school'], foreign_school.name)
