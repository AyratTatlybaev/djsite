from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения report")


def month(request, month_id):
    return HttpResponse(f"<h1>Месяцы</h1><p>{month_id}</p>")