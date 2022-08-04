from django import forms
from .models import *


# класс формы, описывающий добавление отчёта
class AddReportForm(forms.Form):
    title = forms.CharField(max_length=255,
                            label='Название концентрата',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    # Содержание компонентов в концентрате
    component_Fe = forms.FloatField(label='Содержание железа')  # Железо
    component_Si = forms.FloatField(label='Содержание кремния')  # Кремний
    component_Al = forms.FloatField(label='Содержание алюминия')  # Алюминий
    component_Ca = forms.FloatField(label='Содержание кальция')  # Кальций
    component_S = forms.FloatField(label='Содержание серы')  # Сера
    report_year = forms.DecimalField(label='Год отчёта')  # Год отчёта
    report_month = forms.DecimalField(label='Месяц отчёта')  # Месяц отчёта
    # Имя создателя отчёта
    author_name = forms.CharField(label='Автор')