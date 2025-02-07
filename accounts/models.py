from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)  # 아이디
    email = models.EmailField(unique=True)  # 이메일
    bio = models.TextField(blank=True, null=True)  # 자기소개 (선택 사항)
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)  # 프로필 사진

    def __str__(self):
        return f"{self.full_name} ({self.username})"

    @property
    def full_name(self):
        """first_name + last_name을 조합하여 full_name 반환"""
        return f"{self.last_name}{self.first_name}".strip()

    def set_full_name(self, full_name):
        """full_name을 입력받아 first_name과 last_name으로 자동 분리"""
        name_parts = full_name.strip().split()
        
        if len(name_parts) == 1:
            self.last_name = ""
            self.first_name = name_parts[0]
        elif len(name_parts) == 2:
            if len(name_parts[0]) > 1:
                self.last_name = name_parts[0]
                self.first_name = name_parts[1]
            else:
                self.last_name = name_parts[0]
                self.first_name = name_parts[1]
        else:
            self.last_name = name_parts[0]
            self.first_name = " ".join(name_parts[1:])
