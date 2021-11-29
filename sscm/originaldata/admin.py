from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

from sscm.core.admin import BaseAdmin
from .models import OriginalMember


class OriginalMemberAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ("firstname", "surname")

    def get_queryset(self, request):
        return OriginalMember.all_objects.all()


admin.site.register(OriginalMember, OriginalMemberAdmin)
