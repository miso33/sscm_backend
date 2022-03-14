from django.contrib import admin

from .models import Payment
from ..core.admin import BaseAdmin
from rangefilter.filters import DateRangeFilter


@admin.register(Payment)
class PaymentAdmin(BaseAdmin):
    exclude = ("status_changed", "is_removed", "status")
    list_display = [
        "user",
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
        'user__individual_profile__first_name',
        'user__individual_profile__last_name',
        'user__group_profile__name',
        'user__student_profile__first_name',
        'user__student_profile__last_name',
    ]
