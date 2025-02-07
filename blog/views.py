from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# ✅ 게시글 목록 조회 (로그인하지 않은 사용자도 볼 수 있음)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

# ✅ 게시글 상세 조회 (로그인하지 않은 사용자도 볼 수 있음)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# ✅ 게시글 작성 (로그인한 사용자만 가능)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # ✅ 작성자를 현재 로그인한 사용자로 설정
        return super().form_valid(form)

# ✅ 게시글 수정 (로그인한 사용자 + 작성자 본인만 가능)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)  # ✅ 본인 글만 수정 가능

# ✅ 게시글 삭제 (로그인한 사용자 + 작성자 본인만 가능)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # ✅ 삭제 확인 페이지 지정
    success_url = reverse_lazy('post_list')  # ✅ 삭제 후 목록으로 이동

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)  # ✅ 본인 글만 삭제 가능