from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import Deanship, Parish


class DeanshipAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display

    def get_queryset(self, request):
        return Deanship.all_objects.all()


class ParishAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display

    def get_queryset(self, request):
        return Parish.all_objects.all()


admin.site.register(Deanship, DeanshipAdmin)
admin.site.register(Parish, ParishAdmin)
