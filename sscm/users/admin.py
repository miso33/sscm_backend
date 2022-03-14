from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "is_staff",
        "date_joined",
        "type"
    )

    list_filter = ("is_staff", "is_active")
    title = "Užívatelia"

    def get_queryset(self, request):
        query_set = super().get_queryset(request)
        if not request.user.is_superuser:
            return query_set.filter(is_superuser=False)
        return query_set

    def get_fieldsets(self, request, obj=None):
        fieldset = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            return (
                (None, {'fields': ('username', 'password')}),
                ("Osobné údaje", {'fields': ('first_name', 'last_name', 'email')}),

                ("Dátumy", {'fields': ('last_login', 'date_joined')}),
            )
        return fieldset


admin.site.register(UserModel, CustomUserAdmin)
