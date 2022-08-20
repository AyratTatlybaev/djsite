import csv

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Avg, F, Max, Min
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tablib import Dataset
import pandas as pd

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить отчёт", 'url_name': 'add_page'},
       #{'title': "Войти", 'url_name': 'login'},
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

    context = {'months_dict': months_dict,
               'reports': reports,
               'menu': menu,
               'title': 'Главная страница',
               'month_id': 0,
               }
    return render(request, 'report/index.html', context=context)


def about(request):
    return render(request, 'report/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        # Форма с заполненными данными
        form = AddReportForm(request.POST)

        #new_data = request.FILES['myfile']
        #form.fields["title"].initial = str(file_import['title'][0])


        #print(form.instance.title)

        # Проверка - корректно ли заполнены данные
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        # Формирование пустой формы
        form = AddReportForm()
        form.fields["author_name"].initial = str(request.user.username)

    return render(request,
                  'report/addpage.html',
                  {'form': form,
                   'title': "Добавление отчёта",
                   'menu': menu})


# def contact(request):
#     return HttpResponse("Обратная связь")


# def login(request):
#     return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Отчёт не найден</h1>')


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

    agg_avg, agg_max, agg_min = {'name': 'Среднее значение'},\
                                {'name': 'Максимальное значение'}, \
                                {'name': 'Минимальное'}

    # Список словарей с именами столбцов
    list_agg_name = [agg_fe, agg_si, agg_al, agg_ca, agg_s]
    # Список словарей с результатами агрегаций
    list_agg = [agg_avg, agg_max, agg_min]

    # проверка есть ли отчёты за месяц
    if len(reports) == 0:
        raise Http404()
    else:
        for agg in list_agg_name:
            # Среднее значение по столбцам Fe, Si, Al, Ca, S
            agg_avg.update(reports.aggregate(Avg(agg.get('name'))))
            # Максимальное значение по столбцам Fe, Si, Al, Ca, S
            agg_max.update(reports.aggregate(Max(agg.get('name'))))
            # Минимальное значение по столбцам Fe, Si, Al, Ca, S
            agg_min.update(reports.aggregate(Min(agg.get('name'))))

    context = {'months_dict': months_dict,
               'reports': reports,
               'menu': menu,
               'title': 'Данные за месяц',
               'month_id': month_id,
               'month_name': months_dict[month_id],
               'list_agg_name': list_agg_name,
               'list_agg': list_agg,
               }
    return render(request, 'report/index.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'report/register.html'
    success_url = reverse_lazy('')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items())) # + list(c_def.items()))

    # вызывается при успешной проверке формы регистрации
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'report/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    # вызов функции если логин и пароль верны
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')