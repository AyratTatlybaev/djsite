from django.db import models
from django.urls import reverse


class Report(models.Model):
    """Представление таблицы отчёта
    по содержанию компонентов в концентрате"""
    # Наименование сырья
    title = models.CharField(max_length=255, verbose_name="Наименование сырья")
    # Содержание компонентов в концентрате
    component_Fe = models.FloatField(verbose_name="Fe")  # Железо
    component_Si = models.FloatField(verbose_name="Si")  # Кремний
    component_Al = models.FloatField(verbose_name="Al")  # Алюминий
    component_Ca = models.FloatField(verbose_name="Ca")  # Кальций
    component_S = models.FloatField(verbose_name="S")  # Сера
    report_year = models.DecimalField(max_digits=4, decimal_places=0, default=2022, verbose_name='Год')  # Год отчёта
    report_month = models.DecimalField(max_digits=2, decimal_places=0,default=1, verbose_name='Месяц')  # Месяц отчёта
    report_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    report_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    # Имя создателя отчёта
    author_name = models.CharField(max_length=255, default='', verbose_name="Автор", )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('report', kwargs={'month_id': self.report_month})

    # Настройка в админ панели
    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        # Сортировка по заголовкам
        ordering = ['title']
