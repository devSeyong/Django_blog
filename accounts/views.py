from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import SignUpForm, CustomAuthenticationForm, ProfileUpdateForm
from .models import User


# ✅ 회원가입 뷰
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")


# ✅ 로그인 뷰
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "accounts/login.html"

    def form_invalid(self, form):
        """로그인 실패 시 사용자 지정 오류 메시지 설정"""
        messages.error(
            self.request,
            "아이디 또는 비밀번호가 잘못되었습니다. 확인 후 다시 시도해주세요.",
        )
        return super().form_invalid(form)


# ✅ 로그아웃 뷰
class CustomLogoutView(LogoutView):
    next_page = "login"


# ✅ 현재 로그인한 사용자의 프로필 조회
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"

    def get_object(self):
        """로그인한 사용자가 자신의 프로필을 조회할 때"""
        return self.request.user


# ✅ 특정 유저의 프로필 조회 (로그인한 사용자만 볼 수 있도록 제한)
class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"  # ✅ 기존 profile.html 재사용

    def get_object(self):
        """로그인한 사용자만 특정 유저의 프로필을 볼 수 있도록 제한"""
        return get_object_or_404(User, pk=self.kwargs.get("pk"))


# ✅ 프로필 수정 뷰 (로그인한 사용자만 수정 가능)
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        """로그인한 사용자가 자신의 프로필을 수정할 때"""
        return self.request.user
