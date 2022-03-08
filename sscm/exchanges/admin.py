from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group

from sscm.core.admin import BaseAdmin
from .models import School, StudentProfile, Document
from ..users.models import User

DEMO_CHOICES = (
    ("SK", "Slovenčina"),
    ("DE", "Nemčina"),
    ("EN", "Angličtina"),
)


@admin.register(Document)
class DocumentAdmin(BaseAdmin):
    pass


class YourForm(forms.ModelForm):
    language = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DEMO_CHOICES,
        label="Jazyky"
    )

    class Meta:
        model = StudentProfile
        exclude = ["status_changed", "is_removed", "status"]


@admin.register(StudentProfile)
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

    def save_model(self, request, obj, form, change):
        obj.user.groups.add(Group.objects.get(name="exchange"))
        obj.user.type = User.Types.EXCHANGE
        obj.status = StudentProfile.Status.INACTIVE
        super(StudentAdmin, self).save_model(request, obj, form, change)


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
