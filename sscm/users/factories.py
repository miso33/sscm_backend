import factory
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"User{n + 110}")
    email = factory.Sequence(lambda n: f"name{n + 110}@email.com")
    password = factory.PostGenerationMethodCall("set_password", "password*1")
    type = "MEMBER"

    class Meta:
        model = UserModel
