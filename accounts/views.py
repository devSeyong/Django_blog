from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from .forms import (
    SignUpForm,
    CustomAuthenticationForm,
    ProfileUpdateForm,
    FindUsernameForm,
)
from .models import User
from blog.models import Post


# ✅ 회원가입 뷰
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_invalid(self, form):
        """회원가입 실패 시 오류 메시지를 추가"""
        messages.error(
            self.request, "회원가입에 실패했습니다. 입력한 정보를 확인해주세요."
        )
        return super().form_invalid(form)


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
    pass


# ✅ 프로필 조회
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user_profile"  # ✅ 템플릿에서 user_profile로 일관되게 사용

    def get_object(self):
        """로그인한 사용자의 프로필을 반환"""
        return self.request.user

    def get_context_data(self, **kwargs):
        """내가 작성한 게시글 목록을 컨텍스트에 추가"""
        context = super().get_context_data(**kwargs)
        context["user_posts"] = Post.objects.filter(author=self.request.user).order_by(
            "-created_at"
        )
        return context


# ✅ 특정 유저의 프로필 조회
class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user_profile"

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.get_object()
        context["is_owner"] = self.request.user == user_profile
        context["user_posts"] = user_profile.post_set.all().order_by(
            "-created_at"
        )  # ✅ 추가
        return context


# ✅ 프로필 수정 뷰
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        """로그인한 사용자가 자신의 프로필을 수정할 때"""
        return self.request.user


# ✅ 아이디 찾기 뷰
class FindUsernameView(View):
    template_name = "accounts/find_user_id.html"

    def get(self, request):
        form = FindUsernameForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]

            users = User.objects.all()
            user = None

            for u in users:
                if u.full_name == full_name and u.email == email:
                    user = u
                    break

            if user:
                # ✅ 아이디 끝 3자리만 마스킹
                masked_username = user.username[:-3] + "***"
                return render(
                    request,
                    self.template_name,
                    {"form": form, "success": True, "masked_username": masked_username},
                )

        return render(request, self.template_name, {"form": form})
