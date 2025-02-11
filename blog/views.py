from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Post, Comment


# ✅ 게시글 목록 조회 (검색 포함)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q", "")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(author__username__icontains=search_query)
            )

        return queryset.order_by("-created_at")  # ✅ 최신순 정렬

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        return context


# ✅ 게시글 상세 조회
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        return context


# ✅ 게시글 작성
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = (
            self.request.user
        )  # ✅ 작성자를 현재 로그인한 사용자로 설정
        return super().form_valid(form)


# ✅ 게시글 수정
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)  # ✅ 본인 글만 수정 가능


# ✅ 게시글 삭제
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"  # ✅ 삭제 확인 페이지 지정
    success_url = reverse_lazy("post_list")  # ✅ 삭제 후 목록으로 이동

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)  # ✅ 본인 글만 삭제 가능


# ✅ 댓글 작성
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get("content")
        if content:
            comment = Comment.objects.create(
                post=post, author=request.user, content=content
            )
            return JsonResponse(
                {
                    "success": True,
                    "comment_id": comment.id,
                    "content": comment.content,
                    "author": comment.author.username,
                }
            )
        return JsonResponse({"success": False}, status=400)


# ✅ 댓글 수정
class EditCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        new_content = request.POST.get("content")
        if new_content:
            comment.content = new_content
            comment.save()
            return JsonResponse(
                {
                    "success": True,
                    "content": comment.content,
                    "author": comment.author.username,
                }
            )
        return JsonResponse({"success": False}, status=400)


# ✅ 댓글 삭제
class DeleteCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        comment.delete()
        return JsonResponse({"success": True})
