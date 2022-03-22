from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from sscm.captcha.views import CaptchaView
from sscm.death_notices.views import DeathNoticeCreateView
from sscm.parishes.views import ParishList
from sscm.video.views import CodeView

admin.site.site_header = "Členská zóna SSCM"
urlpatterns = (
        [
            path("account-confirm-email/<str:key>/", ConfirmEmailView.as_view()),
            path("admin/", admin.site.urls),
            path("account/", include("dj_rest_auth.urls")),
            path("account/registration/", include("dj_rest_auth.registration.urls")),
            path("login/", LoginView.as_view()),
            path("logout/", LogoutView.as_view()),
            path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
            path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
            path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
            path("parishes/", ParishList.as_view(), name="parish-list"),
            path("death-note/", DeathNoticeCreateView.as_view(), name="death-note-create"),
            path("exchange/", include("sscm.exchanges.urls")),
            path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
            path(
                "dj-rest-auth/account-confirm-email/",
                VerifyEmailView.as_view(),
                name="account_email_verification_sent",
            ),
            re_path(
                r"^account-confirm-email/(?P<key>[-:\w]+)/$",
                VerifyEmailView.as_view(),
                name="account_confirm_email",
            ),
            path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
            path(
                'password-reset-confirm/<uidb64>/<token>/',
                PasswordResetConfirmView.as_view(),
                name='password_reset_confirm'
            ),
            path(
                'password-reset-confirm/',
                PasswordResetConfirmView.as_view(),
                # name='password_reset_confirm'
            ),
            path(
                'password-change/',
                PasswordChangeView.as_view(),
                name='password_reset_complete'
            ),
            path("captcha/", CaptchaView.as_view()),
            path("video/", CodeView.as_view(), name="get_code"),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
