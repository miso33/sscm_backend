from django.contrib import admin

from .models import Payment
from ..core.admin import BaseAdmin
from rangefilter.filters import DateRangeFilter


@admin.register(Payment)
class PaymentAdmin(BaseAdmin):
    exclude = ("status_changed", "is_removed", "status")
    list_display = [
        "member",
        "date",
        "sum",
        "method",
        "document_number",
        "gift",
        "membership"
    ]
    list_filter = [
        "method",
        "gift",
        "membership",
        ('date', DateRangeFilter)
    ]
    search_fields = [
        'member__individual_profile__first_name',
        'member__individual_profile__last_name',
        'member__group_profile__name',
        'member__students__first_name',
        'member__students__last_name',
    ]
