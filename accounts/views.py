from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm
from .models import User

# ✅ 회원가입 뷰 (CBV)
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")  # 회원가입 후 로그인 페이지로 이동

# ✅ 로그인 뷰 (CBV)
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

# ✅ 로그아웃 뷰 (CBV)
class CustomLogoutView(LogoutView):
    next_page = "login"  # 로그아웃 후 로그인 페이지로 이동
