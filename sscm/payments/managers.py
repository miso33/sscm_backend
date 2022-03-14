from django.db import models

from model_utils.managers import QueryManager, SoftDeletableManager, SoftDeletableQuerySet


class PaymentQuerySet(SoftDeletableQuerySet):
    # use_for_related_fields = True
    pass

class PaymentManager(SoftDeletableManager):
    use_for_related_fields = True

    def get_queryset(self):
        return PaymentQuerySet(self.model, using=self._db).filter(is_removed=False)
