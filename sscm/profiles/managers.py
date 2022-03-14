from django.db import models
from model_utils.managers import QueryManager, SoftDeletableManager, SoftDeletableQuerySet


class MemberProfileQuerySet(SoftDeletableQuerySet):
    pass
    # use_for_related_fields = True


class MemberProfileManager(SoftDeletableManager):
    use_for_related_fields = True

    def get_queryset(self):
        return MemberProfileQuerySet(self.model, using=self._db).filter(is_removed=False)
