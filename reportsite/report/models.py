from django.db import models


class Report(models.Model):
    """Представление таблицы отчёта
    по содержанию компонентов в концентрате"""
    # Наименование сырья
    title = models.CharField(max_length=255, verbose_name="Наименование сырья")
    # Содержание компонентов в концентрате (2 цифры после запятой)
    component_Fe = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Fe")  # Железо
    component_Si = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Si")  # Кремний
    component_Al = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Al")  # Алюминий
    component_Ca = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ca")  # Кальций
    component_S = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="S")  # Сера
    report_year = models.DecimalField(max_digits=4, decimal_places=0, default=2022, verbose_name='Год')  # Год отчёта
    report_month = models.DecimalField(max_digits=2, decimal_places=0, default=1, verbose_name='Месяц')  # Месяц отчёта
    report_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    report_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    # Имя создателя отчёта
    author_name = models.CharField(max_length=255, default='', verbose_name="Автор")

    def __str__(self):
        return self.title
