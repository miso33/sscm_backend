from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from sscm.core.admin import BaseAdmin
from .models import GroupProfile, IndividualProfile, MemberProfile

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
    fields = ["name", "user"]

    def get_queryset(self, request):
        return GroupProfile.all_objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "Skupiny"}
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(IndividualProfile)
class IndividualProfileAdmin(ProfileAdmin):
    list_display = ("status", "member_type", "first_name", "last_name", "parish") + ProfileAdmin.list_display
    search_fields = ["first_name", "last_name"]
    list_filter = ["status"]

    # inlines = [CustomInlineUserAdmin]

    def get_queryset(self, request):
        return IndividualProfile.objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "Jednotlivci"}
        return super().changelist_view(request, extra_context=extra_context)

# @admin.register(IndividualProfile)
# class MemberProfileAdmin(MemberProfile):
#     pass
