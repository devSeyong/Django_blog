from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),  # 게시글 목록 조회
    # path("post/<int:pk>/", views.post_detail, name="post_detail"),  # 게시글 상세 조회
    # path("post/write/", views.post_create, name="post_create"),  # 게시글 작성
    # path("post/edit/<int:pk>/", views.post_edit, name="post_edit"),  # 게시글 수정
    # path("post/delete/<int:pk>/", views.post_delete, name="post_delete"),  # 게시글 삭제
]
