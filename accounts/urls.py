from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, ProfileView, UserProfileView, ProfileEditView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),  # 로그인한 사용자 프로필 조회
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),  # 로그인한 사용자 프로필 수정
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),  # 특정 유저 프로필 조회 (로그인 필요)
]