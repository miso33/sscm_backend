from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from sscm.profiles.services import SelectProfileCreateService

UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    @transaction.atomic
    def save(self, arg):
        return super(CustomRegisterSerializer, self).save(arg)

    def custom_signup(self, request, user):
        if "profile" in request.data:
            profile_class = SelectProfileCreateService().get_class(
                request.data["profile"]
            )
            profile_instance = profile_class(request.data["profile"], user)
            if profile_instance.validate():
                profile_instance.save()
            else:
                raise serializers.ValidationError(profile_instance.errors())
