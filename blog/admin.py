from django.contrib import admin
from .models import Category, Post

# Category 모델 간단 등록
admin.site.register(Category)

# Post 모델 간단 등록
admin.site.register(Post)
