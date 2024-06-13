# Generated by Django 5.0.6 on 2024-06-13 12:33

import django.db.models.deletion
import rules.contrib.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('investment_object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemCategory',
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
                    'external_id',
                    models.CharField(
                        max_length=255, unique=True, verbose_name='Id объекта'
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
            ],
            options={
                'verbose_name': 'Категория проблемы',
                'verbose_name_plural': 'Категории проблем',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProblemSubcategory',
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
                    'external_id',
                    models.CharField(
                        max_length=255, unique=True, verbose_name='Id объекта'
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
                (
                    'problem_category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='problem_subcategories',
                        to='support.problemcategory',
                        verbose_name='Категория проблемы',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Подкатегория проблемы',
                'verbose_name_plural': 'Подкатегории проблем',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProblemTheme',
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
                    'external_id',
                    models.CharField(
                        max_length=255, unique=True, verbose_name='Id объекта'
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
                (
                    'problem_subcategory',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='problem_themes',
                        to='support.problemsubcategory',
                        verbose_name='Подкатегория проблемы',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Тема проблемы',
                'verbose_name_plural': 'Темы проблем',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Problem',
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
                    'external_id',
                    models.CharField(max_length=255, verbose_name='Id объекта'),
                ),
                ('name', models.TextField(verbose_name='Название проблемы')),
                (
                    'additional_info',
                    models.TextField(
                        blank=True, verbose_name='Дополнительная информация'
                    ),
                ),
                (
                    'url',
                    models.CharField(
                        max_length=255, verbose_name='Ссылка на объект'
                    ),
                ),
                (
                    'problem_theme',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='problems',
                        to='support.problemtheme',
                        verbose_name='Тема проблемы',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Проблема',
                'verbose_name_plural': 'Проблемы',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServiceSupport',
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
                    'external_id',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Id объекта'
                    ),
                ),
                (
                    'region',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Регион'
                    ),
                ),
                (
                    'service_support_type',
                    models.CharField(
                        choices=[
                            ('service', 'Услуга'),
                            ('support_measure', 'Мера поддержки'),
                        ],
                        max_length=255,
                        verbose_name='Тип сервиса',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Название'
                    ),
                ),
                (
                    'support_type',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Тип поддержки'
                    ),
                ),
                (
                    'support_level',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Уровень поддержки',
                    ),
                ),
                (
                    'description',
                    models.TextField(blank=True, verbose_name='Описание'),
                ),
                (
                    'legal_act',
                    models.TextField(blank=True, verbose_name='Реквизиты НПА'),
                ),
                (
                    'url_legal_act',
                    models.TextField(blank=True, verbose_name='Ссылка на НПА'),
                ),
                (
                    'url_application_form',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Ссылка на форму подачи заявки',
                    ),
                ),
                (
                    'name_responsible_body',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Наименование ответственного органа власти, администрирующего данную меру поддержки',
                    ),
                ),
                (
                    'msp_roster',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Требуется вхождение в реестр МСП',
                    ),
                ),
                (
                    'applicant_requirement',
                    models.TextField(
                        blank=True, verbose_name='Требование к заявителю'
                    ),
                ),
                (
                    'applicant_procedure',
                    models.TextField(
                        blank=True, verbose_name='Процедура подачи заявки'
                    ),
                ),
                (
                    'required_document',
                    models.TextField(
                        blank=True, verbose_name='Необходимые документы'
                    ),
                ),
                (
                    'url',
                    models.CharField(
                        blank=True, verbose_name='Ссылка на объект'
                    ),
                ),
                (
                    'economic_activities',
                    models.ManyToManyField(
                        blank=True,
                        related_name='supports',
                        to='investment_object.economicactivity',
                        verbose_name='Экономическая деятельность',
                    ),
                ),
                (
                    'restrictions',
                    models.ManyToManyField(
                        blank=True,
                        related_name='supports',
                        to='investment_object.restriction',
                        verbose_name='Ограничения по видам деятельности',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Сервис поддержки',
                'verbose_name_plural': 'Сервисы поддержки',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='servicesupport',
            constraint=models.CheckConstraint(
                check=models.Q(
                    ('service_support_type__in', ['service', 'support_measure'])
                ),
                name='service_support_type_valid',
            ),
        ),
    ]
