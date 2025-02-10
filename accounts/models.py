from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse  # ✅ URL 역방향 매핑
from django.utils.timezone import now, timedelta
import random


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )
    reset_code = models.CharField(max_length=6, blank=True, null=True)
    reset_code_expiry = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name}{self.first_name} ({self.username})"

    @property
    def full_name(self):
        """first_name + last_name을 조합하여 full_name 반환"""
        return f"{self.last_name} {self.first_name}".strip()

    def set_full_name(self, full_name):
        """full_name을 입력받아 first_name과 last_name으로 자동 분리"""
        name_parts = full_name.strip().split()

        if len(name_parts) == 1:
            self.last_name = ""
            self.first_name = name_parts[0]
        elif len(name_parts) == 2:
            self.last_name = name_parts[0]
            self.first_name = name_parts[1]
        else:
            self.last_name = name_parts[0]
            self.first_name = " ".join(name_parts[1:])

    def get_absolute_url(self):
        """작성자의 프로필 페이지로 이동하는 URL 반환"""
        return reverse("user_profile", args=[self.pk])  # ✅ URL 역방향 매핑

    def generate_reset_code(self):
        """6자리 랜덤 숫자 생성 후 저장"""
        code = str(random.randint(100000, 999999))  # 6자리 랜덤 코드 생성
        self.reset_code = code
        self.reset_code_expiry = now() + timedelta(minutes=10)  # 10분 후 만료
        self.save()
        return code

    def is_reset_code_valid(self, code):
        """입력한 코드가 맞고, 만료되지 않았는지 확인"""
        return self.reset_code == code and self.reset_code_expiry > now()
