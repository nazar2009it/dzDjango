from django.http import HttpRequest, HttpResponse


def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello World</h1>")


def me(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Nazar</h1>")