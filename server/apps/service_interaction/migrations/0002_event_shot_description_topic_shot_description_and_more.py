# Generated by Django 5.0.6 on 2024-06-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_interaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='shot_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='topic',
            name='shot_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
