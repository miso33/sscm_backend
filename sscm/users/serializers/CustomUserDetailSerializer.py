from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import Field

from sscm.profiles.services import ReadProfileService

UserModel = get_user_model()


class ProfileField(Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data


class CustomUserDetailSerializer(UserDetailsSerializer):
    profile = ProfileField()
    username = serializers.CharField(read_only=True)

    class Meta:
        model = UserModel
        fields = UserDetailsSerializer.Meta.fields + ("profile",)

    @staticmethod
    def get_profile(obj):
        return ReadProfileService().get_serializer(obj)

    def update(self, instance, validated_data):
        if hasattr(instance, "group_profile"):
            instance.group_profile.name = validated_data["profile"]["name"]
            instance_profile = instance.group_profile
        if hasattr(instance, "individual_profile"):
            instance.individual_profile.first_name = validated_data["profile"][
                "first_name"
            ]
            instance.individual_profile.last_name = validated_data["profile"][
                "last_name"
            ]
            instance.individual_profile.birth_date = validated_data["profile"][
                "address"
            ]
            instance.individual_profile.profession = validated_data["profile"][
                "profession"
            ]
            instance.individual_profile.title_prefix = validated_data["profile"][
                "title_prefix"
            ]
            instance.individual_profile.title_suffix = validated_data["profile"][
                "title_suffix"
            ]
            instance_profile = instance.individual_profile
        instance_profile.parish_id = validated_data["profile"]["parish"]
        instance_profile.city = validated_data["profile"]["city"]
        instance_profile.address = validated_data["profile"]["address"]
        instance_profile.zip = validated_data["profile"]["zip"]
        instance.save()
        return instance
