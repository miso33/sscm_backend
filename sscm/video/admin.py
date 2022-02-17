from django.contrib import admin

from .models import Video
from ..core.admin import BaseAdmin


@admin.register(Video)
class VideoAdmin(BaseAdmin):
    exclude = BaseAdmin.exclude + ('status',)
    list_display = ["code", "created"]
