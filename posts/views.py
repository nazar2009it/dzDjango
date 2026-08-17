from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from posts.models import Post


def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello World</h1>")


def me(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Nazar</h1>")


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(is_active=True)
    return render(request, "posts.html", {"posts": posts})