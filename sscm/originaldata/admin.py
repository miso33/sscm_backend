from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import OriginalMember


class OriginalMemberAdmin(BaseAdmin):
    list_display = ("firstname", "surname", "farnost_id")
    search_fields = ["firstname", "surname"]
    list_filter = ["status", "druh_clenstva"]
    title = "Pôvodné údaje členov"

    def get_queryset(self, request):
        return OriginalMember.all_objects.all()


admin.site.register(OriginalMember, OriginalMemberAdmin)
