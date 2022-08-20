from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


# класс формы, описывающий добавление отчёта
class AddReportForm(forms.ModelForm):
    class Meta:
        model = Report
        # Поля для ввода
        fields = ['title',
                  'component_Fe',
                  'component_Si',
                  'component_Al',
                  'component_Ca',
                  'component_S',
                  'report_year',
                  'report_month',
                  'author_name']
        # Стили оформления
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_input'}),

        }

    # Пользовательский валидатор - поле title
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title

    # Пользовательский валидатор - поле component_Fe
    def clean_component_Fe(self):
        component_Fe = self.cleaned_data['component_Fe']
        if component_Fe > 100.0:
            raise ValidationError('Значение превышает 100.0 %')
        return component_Fe


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input-2'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input-2'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input-2'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input-2'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input-2'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input-2'}))
