from django.db.models import F

from sscm.profiles.serializers import GroupExistsProfileSerializer
from .profile_create_service import ProfileCreateService
from ...originaldata.models import OriginalMember


class ExistsGroupCreateService(ProfileCreateService):
    def get_profile_serializer(self):
        return GroupExistsProfileSerializer(data=self.get_data())

    def get_data(self):
        original_member = (
            OriginalMember.objects.filter(
                surname__iexact=self.profile_data["name"]
            ).values(
                "status",
                parish=F("farnost_id"),
                city=F("obec"),
                address=F("adresa"),
                zip=F("psc"),
                member_type=F("druh_clenstva"),
                enter_date=F("datum_vstupu"),
                member_number=F("cl_cislo"),
                note=F("poznamka"),
            ).get()
        )

        return {**self.profile_data, **original_member}
