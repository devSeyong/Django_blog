from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# User 모델 간단 등록
admin.site.register(User, UserAdmin)
