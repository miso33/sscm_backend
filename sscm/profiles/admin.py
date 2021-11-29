from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import GroupProfile, IndividualProfile, MemberProfile


class GroupProfileAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display

    def get_queryset(self, request):
        return GroupProfile.all_objects.all()


class IndividualProfileAdmin(BaseAdmin):
    list_display = ("status", "member_type", "first_name", "last_name", "member_type")

    def get_queryset(self, request):
        return IndividualProfile.objects.all()


class MemberProfileAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display

    def get_queryset(self, request):
        return MemberProfile.all_objects.all()


admin.site.register(GroupProfile, GroupProfileAdmin)
admin.site.register(IndividualProfile, IndividualProfileAdmin)
# admin.site.register(MemberProfile, MemberProfileAdmin)
