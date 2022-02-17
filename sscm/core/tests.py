from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework.test import APITestCase, URLPatternsTestCase

User = get_user_model()


class BaseAPITestCase(APITestCase, URLPatternsTestCase):
    def login_with_all_permissions(self, user, group_name="admin"):
        group = Group.objects.get_or_create(name=group_name)
        for p in Permission.objects.all():
            group[0].permissions.add(p)
        user.groups.add(group[0])
        self.client.force_authenticate(
            user=user
        )
