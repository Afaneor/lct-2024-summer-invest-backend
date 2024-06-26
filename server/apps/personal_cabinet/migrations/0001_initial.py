# Generated by Django 5.0.6 on 2024-06-13 12:33

import django.db.models.deletion
import rules.contrib.models
from django.conf import settings
from django.db import migrations, models

import server.apps.services.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('investment_object', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
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
                    models.CharField(
                        max_length=255, unique=True, verbose_name='Название'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Subscription',
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
                    'subscription_type',
                    models.CharField(
                        choices=[
                            ('investment_object', 'Инвестиционный объект'),
                            ('service_support', 'Сервис поддержки'),
                            ('topic', 'Тема'),
                            ('event', 'События'),
                        ],
                        max_length=255,
                        verbose_name='Тип подписки',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        max_length=255, verbose_name='Почта пользователя'
                    ),
                ),
                (
                    'telegram_username',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Никнейм пользователя в телеграмме',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SubSector',
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
                    models.CharField(
                        max_length=255, unique=True, verbose_name='Название'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Подотрасль',
                'verbose_name_plural': 'Подотрасли',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TerritorialLocation',
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
                    'short_name',
                    models.CharField(
                        max_length=255, verbose_name='Короткое название'
                    ),
                ),
                (
                    'full_name',
                    models.CharField(
                        max_length=255, verbose_name='Полное название'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Территориальное расположение',
                'verbose_name_plural': 'Территориальное расположения',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Business',
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
                    'position',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Должность пользователя в бизнесе',
                    ),
                ),
                (
                    'business_type',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('legal', 'Юридическое лицо'),
                            ('individual', 'Индивидуальный предприниматель'),
                            ('physical', 'Физическое лицо'),
                        ],
                        max_length=255,
                        verbose_name='Тип бизнеса',
                    ),
                ),
                (
                    'inn',
                    models.CharField(
                        blank=True,
                        max_length=12,
                        validators=[
                            server.apps.services.validators.inn_validator
                        ],
                        verbose_name='ИНН физического лица, ИП или компания',
                    ),
                ),
                (
                    'hid',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Уникальный id контрагента в dadata',
                    ),
                ),
                (
                    'short_business_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Короткое название ИП или компании',
                    ),
                ),
                (
                    'full_business_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Полное название ИП или компании',
                    ),
                ),
                (
                    'management_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='ФИО руководителя, только для компании',
                    ),
                ),
                (
                    'management_position',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Должность руководителя, только для компании',
                    ),
                ),
                (
                    'full_opf',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Полное наименование правовой формы',
                    ),
                ),
                (
                    'short_opf',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Короткое наименование правовой формы',
                    ),
                ),
                (
                    'okved_code',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Код ОКВЕД'
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Имя'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Фамилия'
                    ),
                ),
                (
                    'middle_name',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Отчество'
                    ),
                ),
                (
                    'address',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Полный адрес'
                    ),
                ),
                (
                    'country',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Страна'
                    ),
                ),
                (
                    'region',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Город'
                    ),
                ),
                (
                    'city_area',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Область, округ',
                    ),
                ),
                (
                    'city_district',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Район'
                    ),
                ),
                (
                    'phone',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Телефон, относящийся к бизнесу',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        blank=True,
                        max_length=255,
                        verbose_name='Email, относящийся к бизнесу',
                    ),
                ),
                (
                    'site',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Сайт, относящийся к бизнесу',
                    ),
                ),
                (
                    'tax_system_type',
                    models.CharField(
                        choices=[
                            ('osn', 'Общая'),
                            ('ysn', 'Упрощенная'),
                            ('patent', 'Патентная'),
                        ],
                        default='osn',
                        max_length=255,
                        verbose_name='Тип системы налогооблажения',
                    ),
                ),
                (
                    'economic_activities',
                    models.ManyToManyField(
                        blank=True,
                        related_name='business',
                        to='investment_object.economicactivity',
                        verbose_name='Экономическая деятельность',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='businesses',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Пользователь',
                    ),
                ),
                (
                    'sector',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='businesses',
                        to='personal_cabinet.sector',
                        verbose_name='Отрасль хозяйственной деятельности',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Бизнес',
                'verbose_name_plural': 'Бизнесы',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SelectionRequest',
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
                    'anonymous_user_id',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='ID анонимного пользователя. Приходит с front',
                    ),
                ),
                (
                    'is_actual',
                    models.BooleanField(
                        default=True,
                        verbose_name='Актуальный ли запрос на подбор или нет',
                    ),
                ),
                (
                    'is_bot_response_waiting',
                    models.BooleanField(
                        default=False,
                        verbose_name='Ожидает ли запрос ответ от бота или нет',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='selection_requests',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Пользователь',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Запрос на подбор',
                'verbose_name_plural': 'Запросы на подборы',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Message',
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
                    'owner_type',
                    models.CharField(
                        choices=[
                            ('user', 'Пользователь'),
                            ('assistant', 'assistant'),
                            ('system', 'Система'),
                        ],
                        default='user',
                        max_length=255,
                        verbose_name='Владелец',
                    ),
                ),
                ('text', models.TextField(verbose_name='Текст')),
                (
                    'user_filter',
                    models.JSONField(
                        blank=True,
                        null=True,
                        verbose_name='Фильтры для инвестиционных объектов от пользователя',
                    ),
                ),
                (
                    'bot_filter',
                    models.JSONField(
                        blank=True,
                        null=True,
                        verbose_name='Фильтры для инвестиционных объектов от бота',
                    ),
                ),
                (
                    'parent',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='children',
                        to='personal_cabinet.message',
                        verbose_name='Родительское сообщение',
                    ),
                ),
                (
                    'selection_request',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='messages',
                        to='personal_cabinet.selectionrequest',
                        verbose_name='Запрос на подбор',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
    ]
