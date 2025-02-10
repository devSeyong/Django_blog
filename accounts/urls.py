from django.urls import path
from .views import (
    SignUpView,
    CustomLoginView,
    CustomLogoutView,
    ProfileView,
    UserProfileView,
    ProfileEditView,
    FindUsernameView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="user_profile"),
    path("find-username/", FindUsernameView.as_view(), name="find_username"),
]
