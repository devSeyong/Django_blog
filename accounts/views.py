from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
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

# ✅ 로그아웃 뷰
class CustomLogoutView(LogoutView):
    next_page = "login"

# ✅ 프로필 조회 뷰
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    
    def get_object(self):
        return self.request.user  # 현재 로그인한 사용자만 조회 가능

# ✅ 프로필 수정 뷰
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile")  

    def get_object(self):
        return self.request.user  # 현재 로그인한 사용자만 수정 가능
