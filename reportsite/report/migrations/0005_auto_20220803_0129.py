# Generated by Django 3.1.4 on 2022-08-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20220802_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_month',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2, verbose_name='Month'),
        ),
    ]
