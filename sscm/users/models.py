from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from sscm.profiles.services import ReadProfileService


class User(AbstractUser):
    class Types(models.TextChoices):
        EXCHANGE = "EXCHANGE"
        MEMBER = "MEMBER"

    base_type = Types.MEMBER
    type = models.CharField(
        max_length=50, choices=Types.choices, default=Types.MEMBER
    )

    @property
    def profile(self):
        return ReadProfileService().get_serializer(self)

#
# class MemberManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(type=User.Types.MEMBER)
#
#
# class Group(User):
#     objects = MemberManager()
#
#     class Meta:
#         proxy = True
#
#     @property
#     def profile(self):
#         return self.group_profile
#
#
# class Individual(User):
#     objects = MemberManager()
#
#     class Meta:
#         proxy = True
#
#     @property
#     def profile(self):
#         return self.individual_profile
#
#
# class StudentManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(type=User.Types.EXCHANGE)
#
#
# class Student(User):
#     base_type = User.Types.EXCHANGE
#     objects = StudentManager()
#
#     class Meta:
#         proxy = True
#
#     @property
#     def profile(self):
#         return self.student_profile
