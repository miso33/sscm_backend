from .exists_group_create_service import ExistsGroupCreateService
from .exists_individual_create_service import ExistsIndividualCreateService
from .unique_group_create_service import UniqueGroupCreateService
from .unique_individual_create_service import UniqueIndividualCreateService


class SelectProfileCreateService:
    @staticmethod
    def get_class(profile_data):
        exists = profile_data.pop("exists")
        return {
            "GROUP-False": UniqueGroupCreateService,
            "BASIC-False": UniqueIndividualCreateService,
            "GROUP-True": ExistsGroupCreateService,
            "BASIC-True": ExistsIndividualCreateService,
        }[f"{profile_data['member_type']}-{exists}"]
