from datetime import datetime

from django.db.models import F

from sscm.profiles.serializers import IndividualExistsProfileSerializer
from .profile_create_service import ProfileCreateService
from ...originaldata.models import OriginalMember


class ExistsIndividualCreateService(ProfileCreateService):
    def get_profile_serializer(self):
        return IndividualExistsProfileSerializer(data=self.get_data())

    def get_data(self):
        original_member = (
            OriginalMember.objects.filter(
                firstname__iexact=self.profile_data["first_name"],
                surname__iexact=self.profile_data["last_name"],
                datum_nar=datetime.strptime(
                    self.profile_data["birth_date"], "%Y-%m-%d"
                ),
            )
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
                profession=F("povolanie"),
                title_prefix=F("titul"),
                title_suffix=F("titul2"),
            )
            .get()
        )
        return {**self.profile_data, **original_member}
