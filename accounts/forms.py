from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# ✅ 회원가입 폼 (UserCreationForm 상속)
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(attrs={"placeholder": "아이디를 입력하세요"}),
    )
    full_name = forms.CharField(
        label="이름",
        widget=forms.TextInput(attrs={"placeholder": "이름을 입력하세요 (예: 홍길동)"}),
    )
    email = forms.EmailField(
        label="이메일",
        widget=forms.EmailInput(attrs={"placeholder": "이메일을 입력하세요"}),
        required=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_full_name(self):
        """이름 최소 2글자 이상 입력하도록 검증"""
        full_name = self.cleaned_data.get("full_name", "").strip()

        if not full_name:
            raise forms.ValidationError("이름을 입력하세요.")

        if len(full_name) < 2:
            raise forms.ValidationError("이름은 최소 2글자 이상 입력해야 합니다.")

        return full_name

    def save(self, commit=True):
        """full_name을 first_name, last_name으로 자동 분리"""
        user = super().save(commit=False)
        full_name = self.cleaned_data["full_name"]
        user.set_full_name(full_name)

        if commit:
            user.save()
        return user


# ✅ 로그인 폼 (AuthenticationForm 상속)
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(attrs={"placeholder": "아이디를 입력하세요"}),
    )
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호를 입력하세요"}),
    )


# ✅ 프로필 수정 폼
class ProfileUpdateForm(forms.ModelForm):
    full_name = forms.CharField(
        label="이름",
        widget=forms.TextInput(attrs={"placeholder": "이름을 입력하세요 (예: 홍길동)"}),
    )
    bio = forms.CharField(
        label="자기소개",
        widget=forms.Textarea(attrs={"placeholder": "자기소개를 입력하세요", "rows": 3}),
        required=False
    )
    profile_image = forms.ImageField(label="프로필 사진", required=False)

    class Meta:
        model = User
        fields = ["full_name", "bio", "profile_image"]

    def save(self, commit=True):
        """full_name을 first_name, last_name으로 자동 분리"""
        user = super().save(commit=False)
        full_name = self.cleaned_data["full_name"]
        user.set_full_name(full_name)

        if commit:
            user.save()
        return user
