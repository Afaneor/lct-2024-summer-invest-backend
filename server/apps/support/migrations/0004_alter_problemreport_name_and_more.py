# Generated by Django 5.0.6 on 2024-06-07 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_alter_problemreport_theme_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemreport',
            name='name',
            field=models.TextField(verbose_name='Название проблемы'),
        ),
        migrations.AlterField(
            model_name='problemreport',
            name='theme_name',
            field=models.CharField(
                max_length=255, verbose_name='Название темы'
            ),
        ),
    ]