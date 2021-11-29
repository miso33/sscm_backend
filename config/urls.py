from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from dj_rest_auth.views import LoginView, LogoutView

from sscm.parishes.views import ParishList
from sscm.users.views import GetOTPView

admin.site.site_header = 'Administrácia členov SSCM'
urlpatterns = [
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path("admin/", admin.site.urls),
    path("account/", include("dj_rest_auth.urls")),
    path("account/registration/", include("dj_rest_auth.registration.urls")),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("parishes/", ParishList.as_view(), name="parish-list"),

    #     path('password-reset/', PasswordResetView.as_view()),
    #     path(‘password - reset - confirm / < uidb64 > / < token > / ',
    # PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),

    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path(
        'dj-rest-auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),
    path("user/captcha/", GetOTPView.as_view())

]