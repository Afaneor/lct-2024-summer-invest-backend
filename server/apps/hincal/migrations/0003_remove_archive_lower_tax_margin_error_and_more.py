# Generated by Django 4.2.1 on 2023-06-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hincal', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive', name='lower_tax_margin_error',
        ),
        migrations.RemoveField(
            model_name='archive', name='upper_tax_margin_error',
        ),
        migrations.AddField(
            model_name='archive',
            name='lower_margin_error',
            field=models.FloatField(
                default=0.85,
                verbose_name='Нижний уровень погрешности для поиска записей',
            ),
        ),
        migrations.AddField(
            model_name='archive',
            name='upper_margin_error',
            field=models.FloatField(
                default=1.15,
                verbose_name='Верхний уровень погрешности для поиска записей',
            ),
        ),
    ]
