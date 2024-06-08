# Generated by Django 5.0.6 on 2024-06-08 00:05

import rules.contrib.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('investment_object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemReport',
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
                    models.IntegerField(
                        verbose_name='Id проблемы на investmoscom.ru'
                    ),
                ),
                (
                    'external_category_id',
                    models.IntegerField(
                        verbose_name='Id категории проблемы на investmoscom.ru'
                    ),
                ),
                (
                    'external_subcategory_id',
                    models.IntegerField(
                        verbose_name='Id подкатегории проблемы на investmoscom.ru'
                    ),
                ),
                (
                    'external_theme_id',
                    models.IntegerField(
                        verbose_name='Id подкатегории проблемы на investmoscom.ru'
                    ),
                ),
                ('name', models.TextField(verbose_name='Название проблемы')),
                (
                    'category_name',
                    models.CharField(
                        max_length=255, verbose_name='Название категории'
                    ),
                ),
                (
                    'subcategory_name',
                    models.CharField(
                        max_length=255, verbose_name='Название подкатегории'
                    ),
                ),
                (
                    'theme_name',
                    models.CharField(
                        max_length=255, verbose_name='Название темы'
                    ),
                ),
                (
                    'additional_info',
                    models.TextField(
                        blank=True, verbose_name='Дополнительная информация'
                    ),
                ),
                (
                    'url',
                    models.CharField(
                        max_length=255, verbose_name='Дополнительная информация'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Сообщение о проблеме',
                'verbose_name_plural': 'Сообщения о проблемах',
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
                    'region',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Регион'
                    ),
                ),
                (
                    'type_service_support',
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
                    'is_msp_roster',
                    models.BooleanField(
                        blank=True,
                        null=True,
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
                    ('type_service_support__in', ['service', 'support_measure'])
                ),
                name='type_service_support_valid',
            ),
        ),
    ]
