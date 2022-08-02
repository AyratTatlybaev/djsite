from django.db.models import Avg, F, Max, Min
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить отчёт", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):
    # Словарь с месяцами
    months_dict = {1: 'Январь',
                   2: 'Февраль',
                   3: 'Март',
                   4: 'Апрель',
                   5: 'Май',
                   6: 'Июнь',
                   7: 'Июль',
                   8: 'Август',
                   9: 'Сентябрь',
                   10: 'Октябрь',
                   11: 'Ноябрь',
                   12: 'Декабрь'}

    reports = Report.objects.all()
    context = {'months': months_dict,
               'reports': reports,
               'menu': menu,
               'title': 'Главная страница',
               'month_selected': 0,
               }
    return render(request, 'report/index.html', context=context)


def about(request):
    return render(request, 'report/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление отчёта")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_report(request, month_id):
    # Словарь с месяцами
    months_dict = {1: 'Январь',
                   2: 'Февраль',
                   3: 'Март',
                   4: 'Апрель',
                   5: 'Май',
                   6: 'Июнь',
                   7: 'Июль',
                   8: 'Август',
                   9: 'Сентябрь',
                   10: 'Октябрь',
                   11: 'Ноябрь',
                   12: 'Декабрь'}

    reports = Report.objects.filter(report_month=month_id)

    agg_fe = {'name': 'component_Fe'}
    agg_si = {'name': 'component_Si'}
    agg_al = {'name': 'component_Al'}
    agg_ca = {'name': 'component_Ca'}
    agg_s = {'name': 'component_S'}
    # Список словарей с результатами агрегаций
    list_agg = [agg_fe, agg_si, agg_al, agg_ca, agg_s]

    # проверка есть ли отчёты за месяц
    if len(reports) == 0:
        raise Http404()
    else:
        # Среднее, максимальное, минимальное значение
        agg_fe = reports.aggregate(value_avg=Avg('component_Fe'),
                                   value_max=Max('component_Fe'),
                                   value_min=Min('component_Fe'))

    context = {'months_dict': months_dict,
               'reports': reports,
               'menu': menu,
               'title': 'Данные за месяц',
               'month_id': month_id,
               'month_name': months_dict[month_id],
               'list_agg': list_agg,
               }
    return render(request, 'report/index.html', context=context)
