# Generated by Django 5.0.6 on 2024-06-08 20:58

import django.db.models.deletion
import rules.contrib.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='EconomicActivity',
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
                    'code',
                    models.CharField(blank=True, verbose_name='Код отрасли'),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=255, verbose_name='Название отрасли'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Экономическая деятельность',
                'verbose_name_plural': 'Экономические деятельности',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Infrastructure',
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
                    'consumption_tariff',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Тариф на потребление',
                    ),
                ),
                (
                    'transportation_tariff',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Тариф на транспортировку',
                    ),
                ),
                (
                    'max_allowable_power',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Максимально допустимая мощность',
                    ),
                ),
                (
                    'free_power',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Свободная мощность',
                    ),
                ),
                (
                    'throughput',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Пропускная способность',
                    ),
                ),
                (
                    'other_characteristics',
                    models.TextField(
                        blank=True, verbose_name='Иные характеристики'
                    ),
                ),
                (
                    'availability',
                    models.CharField(
                        choices=[
                            ('possible_creation', 'Возможно создание'),
                            ('yes', 'Да'),
                            ('not_data', 'Нет данных'),
                        ],
                        default='not_data',
                        max_length=255,
                        verbose_name='Наличие',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Инфраструктура',
                'verbose_name_plural': 'Инфраструктуры',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvestmentObject',
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
                        blank=True, max_length=255, verbose_name='Наименование'
                    ),
                ),
                (
                    'main_photo_url',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Изображение объекта',
                    ),
                ),
                (
                    'photo_urls',
                    models.JSONField(
                        blank=True,
                        null=True,
                        verbose_name='Дополнительные изображения',
                    ),
                ),
                (
                    'object_type',
                    models.CharField(
                        choices=[
                            ('technopark', 'Технопарк'),
                            ('technopolis', 'Технополис'),
                            ('land_plot', 'Земельный участок'),
                            ('building', 'Помещение'),
                            ('cdt', 'КРТ'),
                            ('tender_lot', 'Лот тендера'),
                            ('ready_business', 'Реальный бизнес'),
                            ('other', 'Другое'),
                            ('not_data', 'Нет данных'),
                        ],
                        default='not_data',
                        verbose_name='Тип объекта',
                    ),
                ),
                (
                    'cost',
                    models.FloatField(null=True, verbose_name='Стоимость'),
                ),
                (
                    'location',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Местоположение',
                    ),
                ),
                (
                    'url',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Ссылка на объект',
                    ),
                ),
                (
                    'longitude',
                    models.DecimalField(
                        decimal_places=3,
                        max_digits=9,
                        null=True,
                        verbose_name='Долгота',
                    ),
                ),
                (
                    'latitude',
                    models.DecimalField(
                        decimal_places=3,
                        max_digits=9,
                        null=True,
                        verbose_name='Широта',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Инвестиционный объект',
                'verbose_name_plural': 'Инвестиционные объекты',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Privilege',
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
            ],
            options={
                'verbose_name': 'Льгота',
                'verbose_name_plural': 'Льготы',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReadyBusiness',
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
                ('description', models.TextField(verbose_name='Описание')),
                (
                    'extra_data',
                    models.JSONField(
                        blank=True,
                        null=True,
                        verbose_name='Дополнительные сведения',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Готовый бизнес',
                'verbose_name_plural': 'Готовые бизнесы',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RealEstate',
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
                    'preferential_treatment',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Преференциальный режим',
                    ),
                ),
                (
                    'preferential_treatment_object_code',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Код объекта преференциального режима',
                    ),
                ),
                (
                    'preferential_treatment_object_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Наименование объекта преференциального режима',
                    ),
                ),
                (
                    'support_infrastructure_object',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Объект инфраструктуры поддержки',
                    ),
                ),
                (
                    'support_infrastructure_object_code',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Код объекта инфраструктуры поддержки',
                    ),
                ),
                (
                    'support_infrastructure_object_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Наименование объекта инфраструктуры поддержки',
                    ),
                ),
                (
                    'region',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Регион'
                    ),
                ),
                (
                    'municipality',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Муниципальное образование',
                    ),
                ),
                (
                    'address',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Адрес администратора объекта',
                    ),
                ),
                (
                    'nearest_cities',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Ближайшие города',
                    ),
                ),
                (
                    'site_format',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Формат площадки',
                    ),
                ),
                (
                    'site_type',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Тип площадки'
                    ),
                ),
                (
                    'ownership_type',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Тип собственности',
                    ),
                ),
                (
                    'rental_period',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Сроки аренды'
                    ),
                ),
                (
                    'procedure_determining_cost',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Порядок определения стоимости',
                    ),
                ),
                (
                    'hazard_class_object',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Класс опасности объекта',
                    ),
                ),
                (
                    'characteristic_object',
                    models.TextField(
                        blank=True,
                        verbose_name='Характеристики расположенных объектов капитального строительства',
                    ),
                ),
                (
                    'land_free_area',
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name='Свободная площадь ЗУ, га',
                    ),
                ),
                (
                    'land_cadastral_number',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Свободная площадь ЗУ, га',
                    ),
                ),
                (
                    'permitted_use_options',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Варианты разрешенного использования',
                    ),
                ),
                (
                    'is_cupping',
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name='Возможность мезжевания',
                    ),
                ),
                (
                    'land_category',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Категория земель',
                    ),
                ),
                (
                    'building_free_area',
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name='Свободная площадь здания, сооружения, помещения, кв. м',
                    ),
                ),
                (
                    'building_cadastral_number',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Кадастровый номер здания, сооружения, помещения',
                    ),
                ),
                (
                    'building_technical_specifications',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Технические характеристики здания, сооружения, помещения',
                    ),
                ),
                (
                    'owner_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Наименование собственника / администратора объекта',
                    ),
                ),
                (
                    'owner_inn',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='ИНН собственника',
                    ),
                ),
                (
                    'owner_website',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Сайт собственника',
                    ),
                ),
                (
                    'other_characteristics',
                    models.TextField(
                        blank=True, verbose_name='Иные характеристики'
                    ),
                ),
                (
                    'application_procedure',
                    models.TextField(
                        blank=True,
                        verbose_name='Описание процедуры подачи заявки',
                    ),
                ),
                (
                    'documents_for_application',
                    models.TextField(
                        blank=True,
                        verbose_name='Перечень документов, необходимых для подачи заявки',
                    ),
                ),
                (
                    'application_form_url',
                    models.TextField(
                        blank=True, verbose_name='Ссылка на форму подачи заявки'
                    ),
                ),
                (
                    'urban_planning',
                    models.TextField(
                        blank=True,
                        verbose_name='Градостроительные характеристики и ограничения',
                    ),
                ),
                (
                    'other_information',
                    models.TextField(blank=True, verbose_name='Иные сведения'),
                ),
                (
                    'is_maip',
                    models.BooleanField(
                        blank=True, null=True, verbose_name='Наличие МАИП'
                    ),
                ),
                (
                    'benefit_description',
                    models.TextField(
                        blank=True, verbose_name='Описание льготы'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимости',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Restriction',
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
                ('name', models.TextField(verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Ограничение по видам деятельности',
                'verbose_name_plural': 'Ограничения по видам деятельности',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SpecializedSite',
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
                    'sez',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Особая экономическая зона',
                    ),
                ),
                (
                    'tad',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Территория опережающего развития',
                    ),
                ),
                (
                    'region',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Регион'
                    ),
                ),
                (
                    'municipality',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Муниципальное образование',
                    ),
                ),
                (
                    'nearest_cities',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Ближайшие города',
                    ),
                ),
                (
                    'number_residents',
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name='Количество резидентов',
                    ),
                ),
                (
                    'document_url',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Документы по объекту',
                    ),
                ),
                (
                    'year_formation',
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name='Год формирования объекта',
                    ),
                ),
                (
                    'validity',
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name='Срок действия объекта',
                    ),
                ),
                (
                    'minimum_rental_price',
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name='Минимальная стоимость аренды, руб./кв.м/год',
                    ),
                ),
                (
                    'total_area',
                    models.FloatField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name='Общая площадь, кв. м',
                    ),
                ),
                (
                    'additional_services',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Дополнительные услуги управляющей компании',
                    ),
                ),
                (
                    'object_administrator_name',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Название администратора объекта',
                    ),
                ),
                (
                    'address',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Адрес администратора объекта',
                    ),
                ),
                (
                    'website',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Ссылка на сайт',
                    ),
                ),
                (
                    'working_hours',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='Время работы'
                    ),
                ),
                (
                    'income_tax',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Налог на прибыль',
                    ),
                ),
                (
                    'property_tax',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Налог на имущество',
                    ),
                ),
                (
                    'land_tax',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Земельный налог',
                    ),
                ),
                (
                    'transport_tax',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Транспортный налог',
                    ),
                ),
                (
                    'insurance_premiums',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Страховые взносы',
                    ),
                ),
                (
                    'is_free_customs_zone_regime',
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name='Наличие режима свободной таможенной зоны',
                    ),
                ),
                (
                    'resident_info',
                    models.TextField(
                        blank=True,
                        verbose_name='Информация о том, как стать новым резидентом',
                    ),
                ),
                (
                    'minimum_investment_amount',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Минимальный объем инвестиций',
                    ),
                ),
                (
                    'urban_planning',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name='Градостроительные характеристики и ограничения',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Специализированная площадка',
                'verbose_name_plural': 'Специализированные площадки',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TenderLot',
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
                    'description',
                    models.TextField(blank=True, verbose_name='Описание'),
                ),
                (
                    'extra_data',
                    models.JSONField(
                        blank=True,
                        null=True,
                        verbose_name='Дополнительные сведения',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Лот тендера',
                'verbose_name_plural': 'Лоты тендера',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TransactionForm',
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
            ],
            options={
                'verbose_name': 'Форма сделки',
                'verbose_name_plural': 'Формы транзакций',
                'ordering': ['-id'],
                'abstract': False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='infrastructure',
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        'availability__in',
                        ['possible_creation', 'yes', 'not_data'],
                    )
                ),
                name='availability_valid',
            ),
        ),
        migrations.AddField(
            model_name='investmentobject',
            name='economic_activities',
            field=models.ManyToManyField(
                blank=True,
                related_name='ready_business',
                to='investment_object.economicactivity',
                verbose_name='Экономическая деятельность',
            ),
        ),
        migrations.AddField(
            model_name='readybusiness',
            name='investment_object',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='ready_business',
                to='investment_object.investmentobject',
                verbose_name='Специализированная площадка',
            ),
        ),
        migrations.AddField(
            model_name='realestate',
            name='infrastructures',
            field=models.ManyToManyField(
                blank=True,
                related_name='real_estates',
                to='investment_object.infrastructure',
                verbose_name='Инфрастуктура',
            ),
        ),
        migrations.AddField(
            model_name='realestate',
            name='investment_object',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='real_estate',
                to='investment_object.investmentobject',
                verbose_name='Специализированная площадка',
            ),
        ),
        migrations.AddField(
            model_name='specializedsite',
            name='infrastructures',
            field=models.ManyToManyField(
                blank=True,
                related_name='specialized_sites',
                to='investment_object.infrastructure',
                verbose_name='Инфрастуктура',
            ),
        ),
        migrations.AddField(
            model_name='specializedsite',
            name='investment_object',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='specialized_site',
                to='investment_object.investmentobject',
                verbose_name='Специализированная площадка',
            ),
        ),
        migrations.AddField(
            model_name='specializedsite',
            name='privileges',
            field=models.ManyToManyField(
                blank=True,
                related_name='specialized_sites',
                to='investment_object.privilege',
                verbose_name='Льготы',
            ),
        ),
        migrations.AddField(
            model_name='specializedsite',
            name='restrictions',
            field=models.ManyToManyField(
                blank=True,
                related_name='specialized_sites',
                to='investment_object.restriction',
                verbose_name='Ограничения по видам деятельности',
            ),
        ),
        migrations.AddField(
            model_name='tenderlot',
            name='investment_object',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='tender_lot',
                to='investment_object.investmentobject',
                verbose_name='Специализированная площадка',
            ),
        ),
        migrations.AddField(
            model_name='investmentobject',
            name='transaction_form',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='ready_business',
                to='investment_object.transactionform',
                verbose_name='Форма сделки',
            ),
        ),
        migrations.AddConstraint(
            model_name='investmentobject',
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        'object_type__in',
                        [
                            'technopark',
                            'technopolis',
                            'land_plot',
                            'building',
                            'cdt',
                            'tender_lot',
                            'ready_business',
                            'other',
                            'not_data',
                        ],
                    )
                ),
                name='object_type_valid',
            ),
        ),
    ]
