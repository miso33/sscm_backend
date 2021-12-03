from django.contrib import admin

from sscm.core.admin import BaseAdmin, BaseStatusAdmin
from .models import GroupProfile, IndividualProfile, MemberProfile


class ProfileAdmin(BaseAdmin):
    list_display = (
        "member_number",
        "parish",
        "status",
        "user_username",
        "date_joined",
    )
    list_filter = ["status"]

    @admin.display(
        description='Používateľské meno',
    )
    def user_username(self, obj):
        return obj.user.username

    @admin.display(
        description='Dátum registrácie',
    )
    def date_joined(self, obj):
        return obj.user.date_joined


class GroupProfileAdmin(ProfileAdmin):
    list_display = ("name",) + ProfileAdmin.list_display
    search_fields = ["name"]
    title = "Skupiny"

    def get_queryset(self, request):
        return GroupProfile.all_objects.all()


class IndividualProfileAdmin(ProfileAdmin):
    list_display = ("first_name", "last_name", "member_type") + ProfileAdmin.list_display
    search_fields = ["first_name", "last_name"]
    title = "Jednotlivci"

    def get_queryset(self, request):
        return IndividualProfile.all_objects.all()


class MemberProfileAdmin(BaseAdmin):
    def get_queryset(self, request):
        return MemberProfile.all_objects.all()


admin.site.register(GroupProfile, GroupProfileAdmin)
admin.site.register(IndividualProfile, IndividualProfileAdmin)
admin.site.register(MemberProfile, MemberProfileAdmin)
