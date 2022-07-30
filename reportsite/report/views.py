from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения report")


def month(request, monthid):
    return HttpResponse(f"<h1>Месяцы</h1><p>{monthid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')