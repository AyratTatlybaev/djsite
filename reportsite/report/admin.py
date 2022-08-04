from django.contrib import admin

from .models import *


# вспомогательный класс для админ панели
class ReportAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'title', 'report_create', 'report_month', 'author_name')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'report_month')
    # поля по которым можно фильтровать
    list_filter = ('report_month', 'author_name')


# Регистрация модели Report, ReportAdmin
admin.site.register(Report, ReportAdmin)
