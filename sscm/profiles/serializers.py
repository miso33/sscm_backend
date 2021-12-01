from rest_framework import serializers
from rest_framework.serializers import Field

from sscm.parishes.serializers import ParishSerializer
from .models import GroupProfile, IndividualProfile, MemberProfile
from ..parishes.models import Parish


class ParishField(Field):
    def to_representation(self, value):
        return ParishSerializer(value).data

    def to_internal_value(self, data):
        return Parish.objects.get(pk=data)


class MemberProfileSerializer(serializers.ModelSerializer):
    member_number = serializers.IntegerField(read_only=True)
    enter_date = serializers.DateField(read_only=True)
    member_type = serializers.CharField()
    status = serializers.CharField(read_only=True)
    parish = ParishField()

    class Meta:
        model = MemberProfile
        fields = [
            "parish",
            "city",
            "address",
            "zip",
            "member_number",
            "enter_date",
            "member_type",
            "status",
        ]


class GroupProfileSerializer(MemberProfileSerializer):
    class Meta:
        model = GroupProfile
        fields = ["name"] + MemberProfileSerializer.Meta.fields


class IndividualProfileSerializer(MemberProfileSerializer):
    class Meta:
        model = IndividualProfile
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "profession",
            "title_prefix",
            "title_suffix",
        ] + MemberProfileSerializer.Meta.fields


class MemberTypeField(Field):
    def to_internal_value(self, data):
        return {"R": "BASIC", "S": "GROUP", "Z": "FOUNDER"}[data]


class StatusField(Field):
    def to_internal_value(self, data):
        return {"A": "ACTIVE", "V": "OUTAGE", "Z": "DECEASED"}[data]


class ExistsProfileSerializer(serializers.ModelSerializer):
    member_number = serializers.IntegerField()
    enter_date = serializers.DateField()
    member_type = MemberTypeField()
    status = StatusField()


class GroupExistsProfileSerializer(ExistsProfileSerializer, GroupProfileSerializer):
    class Meta:
        model = GroupProfileSerializer.Meta.model
        fields = GroupProfileSerializer.Meta.fields + ["note"]


class IndividualExistsProfileSerializer(
    ExistsProfileSerializer, GroupProfileSerializer
):
    class Meta:
        model = IndividualProfileSerializer.Meta.model
        fields = IndividualProfileSerializer.Meta.fields + ["note"]
