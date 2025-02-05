from django.contrib.auth.models import AbstractUser
from django.db import models


# 사용자 모델 (AbstractUser 상속, 기본 기능만 사용)
class User(AbstractUser):
    pass  # 기본 필드(username, email, password, is_active, is_staff 등)만 사용
