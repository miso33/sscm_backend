from abc import ABC, abstractmethod


class ProfileCreateService(ABC):
    def __init__(self, profile_data, user):
        self.profile_data = profile_data
        self.user = user
        self.profile_serializer = self.get_profile_serializer()

    def validate(self):
        return self.profile_serializer.is_valid()

    @abstractmethod
    def get_profile_serializer(self):
        return None

    def save(self):
        return self.profile_serializer.save(user=self.user)

    def errors(self):
        return self.profile_serializer.errors
