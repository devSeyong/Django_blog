from django.db import models
from accounts.models import User  # 사용자 모델 참조


# 게시글 모델
class Post(models.Model):
    title = models.CharField(max_length=255)  # 게시글 제목
    content = models.TextField()  # 게시글 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # null 허용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title
