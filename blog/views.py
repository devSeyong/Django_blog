from django.shortcuts import render

# ✅ 게시글 목록 조회 (CBV 또는 FBV)
def post_list(request):
    return render(request, 'blog/post_list.html')