from django.db.models import F

from sscm.profiles.serializers import GroupExistsProfileSerializer
from .profile_create_service import ProfileCreateService
from ...originaldata.models import OriginalMember

from rest_framework import serializers


class ExistsGroupCreateService(ProfileCreateService):
    def get_profile_serializer(self):
        return GroupExistsProfileSerializer(data=self.get_data())

    def get_data(self):
        original_member = (
            OriginalMember.objects.filter(surname__iexact=self.profile_data["name"])
                .values(
                "status",
                parish=F("farnost_id"),
                city=F("obec"),
                address=F("adresa"),
                zip=F("psc"),
                member_type=F("druh_clenstva"),
                enter_date=F("datum_vstupu"),
                member_number=F("cl_cislo"),
                note=F("poznamka"),
            )
        )

        if not original_member.exists():
            raise serializers.ValidationError(
                {"data": "Zadaný člen sa nenachádza v stare databáze."}
            )
        elif original_member.count() > 1:
            raise serializers.ValidationError(
                {"data": "Zadaný člen sa nachádza v stare databáze viackrát."}
            )
        return {**self.profile_data, **original_member.get()}
