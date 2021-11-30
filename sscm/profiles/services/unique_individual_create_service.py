from sscm.profiles.serializers import IndividualProfileSerializer
from .profile_create_service import ProfileCreateService


class UniqueIndividualCreateService(ProfileCreateService):
    def get_profile_serializer(self):
        return IndividualProfileSerializer(data=self.profile_data)
