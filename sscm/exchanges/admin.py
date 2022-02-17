from django.contrib import admin

from sscm.core.admin import BaseAdmin
from .models import School, Student
from django import forms

# class DecadeBornListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('decade born')
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'decade'
#
#     def lookups(self, request, model_admin):
#         return (
#             ('birthday', _('Oslávenci (tento mesiac)')),
#             ('90s', _('in the nineties')),
#         )
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value() == '80s':
#             return queryset.filter(birthday__gte=date(1980, 1, 1),
#                                     birthday__lte=date(1989, 12, 31))
#         if self.value() == '90s':
#             return queryset.filter(birthday__gte=date(1990, 1, 1),
#                                     birthday__lte=date(1999, 12, 31))
#


DEMO_CHOICES = (
    ("SK", "Slovenčina"),
    ("DE", "Nemčina"),
    ("EN", "Angličtina"),
)


class YourForm(forms.ModelForm):
    language = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DEMO_CHOICES,
        label="Jazyky"
    )

    class Meta:
        model = Student
        exclude = ["status_changed", "is_removed", "status"]


@admin.register(Student)
class StudentAdmin(BaseAdmin):
    exclude = ["member", "status_changed", "is_removed", "status"]
    form = YourForm
    list_display = [
        "first_name",
        "last_name",
        "home_school",
        "foreign_school",
        "semester"
    ]
    list_filter = ["semester", "home_country", "residence_country"]
    search_fields = ["first_name", "last_name"]


@admin.register(School)
class SchoolAdmin(BaseAdmin):
    exclude = ("status",) + BaseAdmin.exclude

    fieldsets = (
        ("Údaje o škole", {
            'fields': (
                "name", "address", "city", "country", "cooperation_start"),
        }),
        ("Kontaktná osoba", {
            'fields': (
                "first_name", "last_name", "phone_number", "email"),
        }),
    )
    list_display = ["name", "address", "city", "country"]
    search_fields = ["name"]
