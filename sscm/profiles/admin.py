from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import GroupProfile, IndividualProfile, MemberProfile


@admin.register(GroupProfile)
class GroupProfileAdmin(BaseAdmin):
    list_display = (
        "name",
        "parish",
        "status",
    )
    search_fields = ["name"]
    list_filter = ["status"]
    fields = ["name", "user"]

    def get_queryset(self, request):
        return GroupProfile.all_objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "Skupiny"}
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(IndividualProfile)
class IndividualProfileAdmin(BaseAdmin):
    list_display = ("status", "member_type", "first_name", "last_name", "parish")
    search_fields = ["first_name", "last_name"]
    list_filter = ["status"]

    def get_queryset(self, request):
        return IndividualProfile.objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "Jednotlivci"}
        return super().changelist_view(request, extra_context=extra_context)

# @admin.register(IndividualProfile)
# class MemberProfileAdmin(MemberProfile):
#     pass
