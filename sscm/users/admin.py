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
    )

    list_filter = ("is_staff", "is_active")

    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        obj.type = UserModel.Types.EXCHANGE
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        query_set = super().get_queryset(request)
        if not request.user.is_superuser:
            return query_set.filter(is_superuser=False)
        return query_set

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "Užívatelia"}
        return super().changelist_view(request, extra_context=extra_context)

    # def get_readonly_fields(self, request, obj=None):
    #     rof = super().get_readonly_fields(request, obj)
    #     if not request.user.is_superuser:
    #         rof += ("is_staff", "is_superuser", "groups", "user_permissions")
    #     return rof
    #
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
