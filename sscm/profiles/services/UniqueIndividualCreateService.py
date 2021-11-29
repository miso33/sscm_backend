from sscm.profiles.serializers import IndividualProfileSerializer
from .ProfileCreateService import ProfileCreateService


class UniqueIndividualCreateService(ProfileCreateService):
    def get_profile_serializer(self):
        return IndividualProfileSerializer(data=self.profile_data)
