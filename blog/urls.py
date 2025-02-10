from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AddCommentView,
    EditCommentView,
    DeleteCommentView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:post_id>/comment/", AddCommentView.as_view(), name="add_comment"),
    path(
        "comment/<int:comment_id>/edit/", EditCommentView.as_view(), name="edit_comment"
    ),
    path(
        "comment/<int:comment_id>/delete/",
        DeleteCommentView.as_view(),
        name="delete_comment",
    ),
]
