from django.contrib import admin
from django.urls import path, include
from blog.views import post_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", post_list, name="post_list"),  # post_list 뷰 연결
    path("blog/", include("blog.urls")),  # blog 앱 연결
    path("accounts/", include("accounts.urls")),  # accounts 앱 연결
]
