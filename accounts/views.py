from django.http import HttpResponse


# 회원가입 뷰
def signup(request):
    return HttpResponse("회원가입 페이지입니다.")


# 로그인 뷰
def login_view(request):
    return HttpResponse("로그인 페이지입니다.")


# 로그아웃 뷰
def logout_view(request):
    return HttpResponse("로그아웃 페이지입니다.")
