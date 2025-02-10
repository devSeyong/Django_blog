from django.urls import path
from .views import (
    SignUpView,
    CustomLoginView,
    CustomLogoutView,
    ProfileView,
    UserProfileView,
    ProfileEditView,
    FindUsernameView,
    PasswordResetRequestView,
    VerifyResetCodeView,
    PasswordResetView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="user_profile"),
    path("find-username/", FindUsernameView.as_view(), name="find_username"),
    path(
        "password-reset-request/",
        PasswordResetRequestView.as_view(),
        name="password_reset_request",
    ),
    path(
        "verify-reset-code/<str:email>/",
        VerifyResetCodeView.as_view(),
        name="verify_reset_code",
    ),
    path(
        "password-reset/<str:email>/<str:code>/",
        PasswordResetView.as_view(),
        name="password_reset",
    ),
]
