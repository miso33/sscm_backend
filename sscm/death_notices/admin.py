from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import DeathNotice


@admin.register(DeathNotice)
class DeathNoticeAdmin(BaseAdmin):
    list_display = (
        "sender",
        "first_name",
        "last_name",
        "birth_date",
    )
