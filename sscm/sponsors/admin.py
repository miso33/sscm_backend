from django.contrib import admin

from .models import Sponsor, Payment
from ..core.admin import BaseAdmin


@admin.register(Sponsor)
class SponsorAdmin(BaseAdmin):
    exclude = ("status_changed", "is_removed", "status")
    list_display = [
        "name",
        "city",
    ]
    search_fields = ["name"]


@admin.register(Payment)
class PaymentAdmin(BaseAdmin):
    exclude = ("status_changed", "is_removed", "status")
    list_display = [
        "sponsor",
        "date",
        "sum",
        "currency",
        "method",
    ]
    list_filter = ["currency", "method"]
    search_fields = ["sponsor__first_name", "sponsor__last_name"]
