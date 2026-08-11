from django.contrib import admin
from django.urls import path
from posts.views import hello_world, me


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello_world),
    path("me/", me),
]