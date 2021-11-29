from sscm.profiles.serializers import GroupProfileSerializer
from .ProfileCreateService import ProfileCreateService


class UniqueGroupCreateService(ProfileCreateService):
    def get_profile_serializer(self):
        return GroupProfileSerializer(data=self.profile_data)
