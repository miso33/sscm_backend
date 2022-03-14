from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group

from sscm.core.admin import BaseAdmin
from .models import School, StudentProfile, Document
from ..users.models import User
from django.contrib.auth.hashers import make_password, check_password

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
    email = forms.CharField()

    class Meta:
        model = StudentProfile
        exclude = ["status_changed", "is_removed", "status"]


@admin.register(StudentProfile)
class StudentAdmin(BaseAdmin):
    form = YourForm
    list_display = [
        "first_name",
        "last_name",
        "home_school",
        "foreign_school",
        "semester",
    ]

    list_filter = ["semester", "home_country", "residence_country"]
    search_fields = ["first_name", "last_name"]

    def get_fields(self, request, obj=None):
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            "city",
            "address",
            "zip",
            "home_school",
            "foreign_school",
            "semester",
            "start",
            "end",
            "phone_number",
            "university_name",
            "university_country",
            "study_filed",
            "language"
        ]
        if obj is None:
            fields = ["email"] + fields
        if request.user.is_superuser or "staff" in request.user.groups.all():
            fields += [
                "parish",
                "member_number",
                "enter_date",
                "member_type",
                # "status",
                "note",
                'profession',
                'title_prefix',
                'title_suffix',
                "death_date",
                "status"
            ]
        return fields

    def save_model(self, request, obj, form, change):
        if not change:
            user = User.objects.create(
                email=request.POST["email"],
                password=make_password("hesloheslo"),
                type=User.Types.EXCHANGE,
                username=request.POST["email"].split("@")[0]
            )
            user.groups.add(Group.objects.get(name="exchange"))
            obj.user = user
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
