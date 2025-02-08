from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


# ✅ 회원가입 폼 (UserCreationForm 상속)
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={"placeholder": "아이디를 입력하세요", "class": "form-control"}
        ),
    )
    full_name = forms.CharField(
        label="이름",
        widget=forms.TextInput(
            attrs={
                "placeholder": "이름을 입력하세요 (예: 홍길동)",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        label="이메일",
        widget=forms.EmailInput(
            attrs={"placeholder": "이메일을 입력하세요", "class": "form-control"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = ["username", "full_name", "email", "password1", "password2"]

    def clean_username(self):
        """아이디 중복 검사"""
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "이미 사용 중인 아이디입니다. 다른 아이디를 입력해주세요."
            )
        return username

    def clean_email(self):
        """이메일 중복 검사"""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "이미 사용 중인 이메일입니다. 다른 이메일을 입력해주세요."
            )
        return email

    def save(self, commit=True):
        """full_name을 User 모델의 set_full_name()을 이용해 저장"""
        user = super().save(commit=False)
        user.set_full_name(self.cleaned_data["full_name"])

        if commit:
            user.save()
        return user


# ✅ 로그인 폼 (AuthenticationForm 상속)
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={"placeholder": "아이디를 입력하세요", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호를 입력하세요", "class": "form-control"}
        ),
    )


# ✅ 프로필 수정 폼
class ProfileUpdateForm(forms.ModelForm):
    full_name = forms.CharField(
        label="이름",
        widget=forms.TextInput(
            attrs={
                "placeholder": "이름을 입력하세요 (예: 홍길동)",
                "class": "form-control",
            }
        ),
    )
    bio = forms.CharField(
        label="자기소개",
        widget=forms.Textarea(
            attrs={
                "placeholder": "자기소개를 입력하세요",
                "rows": 3,
                "class": "form-control",
            }
        ),
        required=False,
    )
    profile_image = forms.ImageField(
        label="프로필 사진",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control"}
        ),  # ✅ Bootstrap 스타일 적용
    )

    class Meta:
        model = User
        fields = ["full_name", "bio", "profile_image"]

    def save(self, commit=True):
        """full_name을 User 모델의 first_name 필드에 저장"""
        user = super().save(commit=False)
        user.first_name = self.cleaned_data[
            "full_name"
        ]  # ✅ set_full_name() 대신 first_name 사용

        if commit:
            user.save()
        return user
