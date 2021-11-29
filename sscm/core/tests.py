from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.conf import settings

User = get_user_model()

#
class BaseAPITestCase(APITestCase, URLPatternsTestCase):
    pass
#     def setUp(self):
#         pass
#
#     def login_with_all_permissions(self, user):
#         group = Group.objects.get_or_create(name="admin")
#         for p in Permission.objects.all():
#             group[0].permissions.add(p)
#         user.groups.add(group[0])
#         self.client.force_authenticate(
#             user=user
#         )
#
#     def login(self, role, user):
#         user.groups.add(Group.objects.filter(name=role).get())
#         self.client.force_authenticate(user=user)
#
