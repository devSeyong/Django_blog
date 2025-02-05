from django.http import HttpResponse


# ✅ 게시글 목록 조회 (테스트용)
def post_list(request):
    return HttpResponse("<h1>게시글 목록 페이지입니다.</h1>")


# ✅ 게시글 상세 조회 (테스트용)
def post_detail(request, pk):
    return HttpResponse(f"<h1>게시글 상세 페이지입니다. (ID: {pk})</h1>")


# ✅ 게시글 작성 (테스트용)
def post_create(request):
    return HttpResponse("<h1>게시글 작성 페이지입니다.</h1>")


# ✅ 게시글 수정 (테스트용)
def post_edit(request, pk):
    return HttpResponse(f"<h1>게시글 수정 페이지입니다. (ID: {pk})</h1>")


# ✅ 게시글 삭제 (테스트용)
def post_delete(request, pk):
    return HttpResponse(f"<h1>게시글 삭제 페이지입니다. (ID: {pk})</h1>")
