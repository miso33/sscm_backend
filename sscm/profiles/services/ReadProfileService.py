from sscm.profiles.serializers import (
    GroupProfileSerializer,
    IndividualProfileSerializer,
)


class ReadProfileService:
    @staticmethod
    def get_serializer(user):
        if hasattr(user, "group_profile"):
            return GroupProfileSerializer(user.group_profile).data
        if hasattr(user, "individual_profile"):
            return IndividualProfileSerializer(user.individual_profile).data
        return None
