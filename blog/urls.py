from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),                        # ✅ 게시글 목록 조회
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),     # ✅ 게시글 상세 조회
    path('post/create/', PostCreateView.as_view(), name='post_create'),       # ✅ 게시글 작성
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # ✅ 게시글 수정
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), # ✅ 게시글 삭제
]