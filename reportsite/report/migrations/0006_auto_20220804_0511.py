# Generated by Django 3.1.4 on 2022-08-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20220803_0129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['title'], 'verbose_name': 'Отчёт', 'verbose_name_plural': 'Отчёты'},
        ),
        migrations.AlterField(
            model_name='report',
            name='author_name',
            field=models.CharField(default='', max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_month',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_year',
            field=models.DecimalField(decimal_places=0, default=2022, max_digits=4, verbose_name='Год'),
        ),
    ]
