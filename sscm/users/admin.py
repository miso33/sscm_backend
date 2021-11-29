from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Užívatelia'}
        return super(CustomUserAdmin, self).changelist_view(request, extra_context=extra_context)

# admin.site.register(UserModel, UserAdmin)
