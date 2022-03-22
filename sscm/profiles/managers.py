from django.db.models import Q, Case, When, F, DateField, CharField
from model_utils.managers import SoftDeletableManager, SoftDeletableQuerySet


class MemberProfileQuerySet(SoftDeletableQuerySet):
    def active(self):
        return self.filter(
            Q(
                individual_profile__isnull=False,
                individual_profile__death_date=None
            ) |
            Q(
                students__isnull=False,
                students__death_date=None
            ),
            status=self.model.Status.ACTIVE,
            leave_date=None,

        )

    def exists_profile_birthday(self):
        return self.annotate(
            birth_date=Case(
                When(
                    individual_profile=None,
                    then=F('students__birth_date')
                ),
                default=F('individual_profile__birth_date'),
                output_field=DateField(),
            ),
            first_name=Case(
                When(
                    individual_profile=None,
                    then=F('students__first_name')
                ),
                default=F('individual_profile__first_name'),
                output_field=CharField(),
            ),
            last_name=Case(
                When(
                    individual_profile=None,
                    then=F('students__last_name')
                ),
                default=F('individual_profile__last_name'),
                output_field=CharField(),
            ),

        ).order_by(
            "birth_date"
        )

    def birthdays_by_month(self, month):
        return self.active().filter(
            Q(
                individual_profile__birth_date__month=month,
            ) |
            Q(
                students__birth_date__month=month,
            ),
        ).exists_profile_birthday()

    def birthdays_by_day(self, date):
        return self.filter(
            Q(
                individual_profile__birth_date=date,
                individual_profile__user__isnull=False,

            ) |
            Q(
                students__birth_date=date,
                students__user__isnull=False,

            )
        ).annotate(
            email=Case(
                When(
                    individual_profile=None,
                    then=F('students__user__email')
                ),
                default=F('individual_profile__user__email'),
                output_field=CharField(),
            ),
        ).exists_profile_birthday()


class MemberProfileManager(SoftDeletableManager):

    def get_queryset(self):
        return MemberProfileQuerySet(self.model, using=self._db).filter(is_removed=False)

    def birthdays_by_month(self, month):
        return self.get_queryset().birthdays_by_month(month).values(
            "first_name",
            "last_name",
            "birth_date"
        )

    def birthdays_by_day(self, date):
        return self.get_queryset().birthdays_by_day(date).values(
            "first_name",
            "last_name",
            "birth_date",
            "email"
        )
