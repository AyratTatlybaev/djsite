from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить отчёт", "Обратная связь", "Войти"]

month_dict = {'1': 'Январь',
              '2': 'Февраль',
              '3': 'Март',
              '4': 'Апрель',
              '5': 'Май',
              '6': 'Июнь',
              '7': 'Июль',
              '8': 'Август',
              '9': 'Сентябрь',
              '10': 'Октябрь',
              '11': 'Ноябрь',
              '12': 'Декабрь'}

def index(request):
    reports = Report.objects.all()
    return render(request, 'report/index.html', {'reports': reports, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'report/about.html', {'menu': menu, 'title': 'О сайте'})


def month(request, monthid):
    return HttpResponse(f"<h1>Месяцы</h1><p>{monthid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')