from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from sscm.core.admin import BaseAdmin
from sscm.notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(BaseAdmin):
    list_display = [
        "recipients",
        "created",
        "sent",
    ]
    list_filter = ("sent", ("created", DateTimeRangeFilter))
