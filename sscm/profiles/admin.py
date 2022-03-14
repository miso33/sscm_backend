from datetime import datetime, date

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.urls import reverse
from django.utils.safestring import mark_safe

from sscm.core.admin import BaseAdmin
from .models import GroupProfile, IndividualProfile, MemberProfile
from ..users.models import User

UserModel = get_user_model()


class ProfileAdmin(BaseAdmin):
    list_display = (
        "member_number",
        "parish",
        "status",
        "user_username",
        "created",
    )
    list_filter = ["status"]

    @admin.display(
        description='Používateľské meno',
    )
    def user_username(self, obj):
        if obj.user is not None:
            return obj.user.username


@admin.register(GroupProfile)
class GroupProfileAdmin(ProfileAdmin):
    list_display = (
                       "name",
                       "parish",
                       "status",
                   ) + ProfileAdmin.list_display
    search_fields = ["name"]
    list_filter = ["status"]
    title = "Skupiny"


@admin.register(IndividualProfile)
class IndividualProfileAdmin(ProfileAdmin):
    list_display = ("member_type", "first_name", "last_name", "parish") + ProfileAdmin.list_display
    search_fields = ["first_name", "last_name"]
    list_filter = ["status"]
    title = "Jednotlivci"


class DefaulterFilter(admin.SimpleListFilter):
    title = "Neplatič"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        actual_year = date.today().year
        year_filter = []
        for year in range(actual_year - 3, actual_year + 4):
            year_filter.append((year, year))
        return year_filter

    def queryset(self, request, queryset):
        if "year" in request.GET:
            year = request.GET["year"]
            return queryset.exclude(
                Q(
                    students__user__payments__date__year=year,
                    students__user__payments__is_removed=False,
                ) |
                Q(
                    individual_profile__user__payments__date__year=year,
                    individual_profile__user__payments__is_removed=False,

                ) |
                Q(
                    group_profile__user__payments__date__year=year,
                    group_profile__user__payments__is_removed=False,
                ) |
                Q(enter_date__gte=datetime.strptime(f"01.10.{year}", '%d.%m.%Y'))
            )
        return queryset.all()


@admin.register(MemberProfile)
class MemberProfileAdmin(BaseAdmin):
    list_display = [
        "author_link",
        "status",
        "member_number",
        "member_type",
        "parish",
        "created",
        "user_username",
    ]

    list_filter = [DefaulterFilter]

    def get_queryset(self, request):
        return MemberProfile.objects.exclude(
            Q(
                students__user__type=User.Types.EXCHANGE,
            )
        )

    @admin.display(
        description='Používateľské meno',
    )
    def user_username(self, obj):
        if hasattr(obj, 'individual_profile') and obj.individual_profile.user is not None:
            return obj.individual_profile.user.username
        if hasattr(obj, 'group_profile') and obj.group_profile.user is not None:
            return obj.group_profile.user.username
        return " "

    @admin.display(
        description='Názov',
    )
    def author_link(self, obj):
        if hasattr(obj, 'group_profile'):
            url = reverse("admin:profiles_groupprofile_change", args=[obj.group_profile.id])
            link = '<a href="%s">%s</a>' % (url, obj.group_profile.name)
            return mark_safe(link)
        if hasattr(obj, 'individual_profile'):
            if obj.individual_profile.first_name and obj.individual_profile.last_name:
                text = f'{obj.individual_profile.first_name} {obj.individual_profile.last_name}'
            else:
                text = obj.individual_profile.id
            url = reverse("admin:profiles_individualprofile_change", args=[obj.individual_profile.id])
            link = '<a href="%s">%s</a>' % (
                url,
                text
            )
            return mark_safe(link)
        if hasattr(obj, 'students'):
            if obj.students.first_name and obj.students.last_name:
                text = f'{obj.students.first_name} {obj.students.last_name}'
            else:
                text = obj.students.id
            url = reverse("admin:exchanges_studentprofile_change", args=[obj.students.id])
            link = '<a href="%s">%s</a>' % (
                url,
                text
            )
            return mark_safe(link)
        return ""
