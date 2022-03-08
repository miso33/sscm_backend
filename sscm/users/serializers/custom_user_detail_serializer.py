from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import Field

from sscm.profiles.services import ReadProfileService
from sscm.users.models import User

UserModel = get_user_model()


class ProfileField(Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class CustomUserDetailSerializer(UserDetailsSerializer):
    profile = ProfileField()
    username = serializers.CharField(read_only=True)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = UserDetailsSerializer.Meta.fields + ("type", "permissions", "profile")

    def get_permissions(self, obj):
        return obj.groups.all().values("name")

    @staticmethod
    def get_profile(value):
        return ReadProfileService().get_serializer(value)

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
                "birth_date"
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
        if hasattr(instance, "student_profile"):
            if "first_name" in validated_data["profile"]:
                instance.student_profile.first_name = validated_data["profile"][
                    "first_name"
                ]
            if "last_name" in validated_data["profile"]:
                instance.student_profile.last_name = validated_data["profile"][
                    "last_name"
                ]
            if "birth_date" in validated_data["profile"]:
                instance.student_profile.birth_date = validated_data["profile"][
                    "birth_date"
                ]
            if "profession" in validated_data["profile"]:
                instance.student_profile.profession = validated_data["profile"][
                    "profession"
                ]
            if "title_prefix" in validated_data["profile"]:
                instance.student_profile.title_prefix = validated_data["profile"][
                    "title_prefix"
                ]
            if "title_suffix" in validated_data["profile"]:
                instance.student_profile.title_suffix = validated_data["profile"][
                    "title_suffix"
                ]
            if "note" in validated_data["profile"]:
                print("note note")
                instance.student_profile.note = validated_data["profile"][
                    "note"
                ]
            instance_profile = instance.student_profile
            if instance.type == User.Types.EXCHANGE and "parish" in validated_data["profile"]:
                instance.type = User.Types.MEMBER

        if "parish" in validated_data["profile"]:
            instance_profile.parish_id = validated_data["profile"]["parish"]
        if "city" in validated_data["profile"]:
            instance_profile.city = validated_data["profile"]["city"]
        if "address" in validated_data["profile"]:
            instance_profile.address = validated_data["profile"]["address"]
        if "zip" in validated_data["profile"]:
            instance_profile.zip = validated_data["profile"]["zip"]
        a = instance.save()
        return instance
