from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import OriginalMember
from ..profiles.models import GroupProfile, IndividualProfile


@admin.register(OriginalMember)
class OriginalMemberAdmin(BaseAdmin):
    title = "Pôvodné údaje členov"
    list_display = ("firstname", "surname", "farnost_id", "is_registered", "get_modified")
    search_fields = ["firstname", "surname"]
    list_filter = ["status", "druh_clenstva"]

    @admin.display(description='Posledná úprava')
    def get_modified(self, obj):
        return obj.modified

    @admin.display(boolean=True, description='Registrovaný')
    def is_registered(self, obj):
        if obj.firstname == "x":
            return GroupProfile.objects.filter(
                name__unaccent__icontains=obj.surname
            ).exists()
        else:
            return IndividualProfile.objects.filter(
                first_name__unaccent__icontains=obj.firstname,
                last_name__unaccent__icontains=obj.surname,
                birth_date=obj.datum_nar,
            ).exists()
