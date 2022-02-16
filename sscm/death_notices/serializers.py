from rest_framework import serializers
from rest_framework.serializers import HiddenField, CurrentUserDefault

from .models import DeathNotice


class DeathNoticeSerializer(serializers.ModelSerializer):
    sender = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = DeathNotice
        fields = [
            "sender",
            "first_name",
            "last_name",
            "birth_date",
        ]
