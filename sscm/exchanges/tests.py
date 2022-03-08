import pytest
from django.urls import include, path
from django.urls import reverse
from rest_framework import status

from .factories import StudentProfileFactory, SchoolFactory, DocumentFactory
from .models import StudentProfile, Document
from ..core.tests import BaseAPITestCase
from ..parishes.factories import ParishFactory
from ..profiles.factories import MemberProfileFactory
from ..users.factories import UserFactory


class DocumentAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("student/", include("sscm.exchanges.urls")),
    ]

    @pytest.mark.document
    def test_list(self):
        self.login_with_all_permissions(user=UserFactory())
        DocumentFactory.create_batch(10)
        response = self.client.get(
            path=reverse("document-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.json()),
            Document.objects.count()
        )

    @pytest.mark.document
    def test_list_not_logged(self):
        DocumentFactory.create_batch(10)
        response = self.client.get(
            path=reverse("document-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.document
    def test_list_wo_permissions(self):
        self.client.force_authenticate(
            user=UserFactory()
        )
        DocumentFactory.create_batch(10)
        response = self.client.get(
            path=reverse("document-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class StudentProfileAPITestCase(BaseAPITestCase):
    urlpatterns = [
        path("student/", include("sscm.exchanges.urls")),
    ]

    @pytest.mark.student
    def test_list(self):
        self.login_with_all_permissions(user=UserFactory())
        StudentProfileFactory.create_batch(10)
        response = self.client.get(
            path=reverse("student-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.json()),
            StudentProfile.objects.count()
        )

    @pytest.mark.student
    def test_list_school_name(self):
        self.login_with_all_permissions(user=UserFactory())
        home_school = SchoolFactory()
        foreign_school = SchoolFactory()
        StudentProfileFactory(
            home_school=home_school,
            foreign_school=foreign_school,
        )
        response = self.client.get(
            path=reverse("student-list"),
        )
        student_response = response.json()[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(student_response['home_school'], home_school.name)
        self.assertEqual(student_response['foreign_school'], foreign_school.name)
    # #
    # @pytest.mark.student
    # @pytest.mark.skip
    # def test_add_to_members(self):
    #     student = StudentProfileFactory()
    #     self.login_with_all_permissions(user=student.user)
    #     # Group.objects.create(name="member")
    #     user = UserFactory()
    #     self.client.force_authenticate(user=user)
    #     response = self.client.put(
    #         path=reverse("rest_user_details"),
    #         data={
    #             "email": user.email,
    #             "profile": {
    #                 "name": new_group_profile.name,
    #                 "parish": original_group_profile.parish.id,
    #                 "city": original_group_profile.city,
    #                 "address": original_group_profile.address,
    #                 "zip": original_group_profile.zip,
    #                 "member_type": "GROUP",
    #             },
    #         },
    #     )
    #     response.json()['results'][0]
    #     # self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(student_response['home_school'], home_school.name)
    #     # self.assertEqual(student_response['foreign_school'], foreign_school.name)
