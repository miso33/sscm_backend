import logging

from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sscm.originaldata.models import OriginalMember
from sscm.profiles.services import SelectProfileCreateService

logger = logging.getLogger(__name__)
UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    @transaction.atomic
    def save(self, request):
        return super().save(request)

    def custom_signup(self, request, user):
        try:
            if "profile" in request.data:
                profile_class = SelectProfileCreateService().get_class(
                    request.data["profile"]
                )
                profile_instance = profile_class(request.data["profile"], user)
                if profile_instance.validate():
                    profile_instance.save()
                else:
                    raise serializers.ValidationError(profile_instance.errors())
        except OriginalMember.DoesNotExist as error:
            logger.error(error)
            raise serializers.ValidationError({"data": "Zadaný člen sa nenachádza v stare databáze."})
        except ValidationError as error:
            logger.error(error)
            raise error
        except MultipleObjectsReturned as error:
            logger.error(error)
            raise serializers.ValidationError({"data": "Zadaný člen sa nenachádza v stare databáze viackrát."})
        except Exception as error:
            logger.error(error)
            raise serializers.ValidationError({"data": "Undefined error"})
