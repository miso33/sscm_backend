from .ExistsIndividualCreateService import ExistsIndividualCreateService
from .ExistsGroupCreateService import ExistsGroupCreateService
from .UniqueGroupCreateService import UniqueGroupCreateService
from .UniqueIndividualCreateService import UniqueIndividualCreateService


class SelectProfileCreateService:

    @staticmethod
    def get_class(profile_data):
        exists = profile_data.pop('exists')
        return {
            "GROUP-False": UniqueGroupCreateService,
            "BASIC-False": UniqueIndividualCreateService,
            "GROUP-True": ExistsGroupCreateService,
            "BASIC-True": ExistsIndividualCreateService,
        }["{0}-{1}".format(profile_data['member_type'], exists)]
