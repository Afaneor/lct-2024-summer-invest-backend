# Generated by Django 5.0.6 on 2024-06-09 16:08

import django.db.models.deletion
import rules.contrib.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Создан'
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(auto_now=True, verbose_name='Изменен'),
                ),
                (
                    'name',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Тема',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Создан'
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(auto_now=True, verbose_name='Изменен'),
                ),
                (
                    'name',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
                (
                    'event_datetime',
                    models.DateTimeField(
                        verbose_name='Время проведения события'
                    ),
                ),
                ('description', models.TextField(verbose_name='Описание')),
                (
                    'event_type',
                    models.CharField(
                        choices=[
                            ('webinar', 'Вебинар'),
                            ('meeting', 'Встреча'),
                        ],
                        max_length=255,
                        verbose_name='Название',
                    ),
                ),
                (
                    'object_id',
                    models.PositiveIntegerField(verbose_name='Id объекта'),
                ),
                (
                    'content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contenttypes.contenttype',
                        verbose_name='Тип содержимого',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Создан'
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(auto_now=True, verbose_name='Изменен'),
                ),
                ('text', models.TextField(verbose_name='Текст')),
                (
                    'object_id',
                    models.PositiveIntegerField(verbose_name='Id объекта'),
                ),
                (
                    'content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contenttypes.contenttype',
                        verbose_name='Тип содержимого',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='feedbacks',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Пользователь',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Создан'
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(auto_now=True, verbose_name='Изменен'),
                ),
                ('text', models.TextField(verbose_name='Текст')),
                (
                    'parent',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='children',
                        to='service_interaction.post',
                        verbose_name='Родительский пост',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='posts',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Пользователь',
                    ),
                ),
                (
                    'topic',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='posts',
                        to='service_interaction.topic',
                        verbose_name='Тема',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(
                check=models.Q(('event_type__in', ['webinar', 'meeting'])),
                name='event_type_valid',
            ),
        ),
    ]
