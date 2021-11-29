from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import OriginalMember


class OriginalMemberAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ("firstname", "surname", "farnost_id")

    def get_queryset(self, request):
        return OriginalMember.all_objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Pôvodné údaje členov'}
        return super(OriginalMemberAdmin, self).changelist_view(request, extra_context=extra_context)


admin.site.register(OriginalMember, OriginalMemberAdmin)
