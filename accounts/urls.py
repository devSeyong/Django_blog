from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # ✅ 회원가입 URL
    path('login/', CustomLoginView.as_view(), name='login'),  # ✅ 로그인 URL
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # ✅ 로그아웃 URL
]