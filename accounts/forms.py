from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# ✅ 회원가입 폼 (UserCreationForm 상속)
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="이메일",
        widget=forms.EmailInput(attrs={"placeholder": "이메일을 입력하세요"}),
    )
    bio = forms.CharField(
        required=False,
        label="소개",
        widget=forms.Textarea(
            attrs={"placeholder": "자기소개를 입력하세요", "rows": 3}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "bio",
        ]  # ✅ 회원가입 폼 필드
