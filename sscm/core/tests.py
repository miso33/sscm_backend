from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, URLPatternsTestCase

User = get_user_model()


#
class BaseAPITestCase(APITestCase, URLPatternsTestCase):
    pass
