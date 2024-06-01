from django.contrib import admin

from server.apps.hincal.models import (
    Archive,
    Business,
    BusinessIndicator,
    Equipment,
    Report,
    Sector,
    Statistic,
    SubSector,
    TerritorialLocation,
)


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin[Archive]):
    """Архив данных."""

    list_display = (
        'id',
        'year',
        'is_actual',
    )
    list_filter = (
        'year',
        'is_actual',
    )
    search_fields = (
        'year',
        'is_actual',
    )
    ordering = (
        'year',
        'is_actual',
    )


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin[Business]):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    list_display = (
        'id',
        'user',
        'type',
        'inn',
        'sector',
        'short_business_name',
    )

    list_filter = (
        'id',
        'type',
        'sector',
        'sub_sector',
    )
    search_fields = (
        'user__email',
        'user__first_name',
        'user_last_name',
        'sector',
        'short_business_name',
        'full_business_name',
        'first_name',
        'last_name',
        'middle_name',
        'address',
        'country',
        'region',
        'city_area',
        'city_district',
        'phone',
        'email',
        'site',
    )
    ordering = (
        'id',
        'type',
        'sector',
        'sub_sector',
    )


@admin.register(BusinessIndicator)
class BusinessIndicatorAdmin(admin.ModelAdmin[BusinessIndicator]):
    """Экономические показатели ИП, физического лица или компании."""

    list_display = (
        'id',
        'business',
        'year',
    )
    list_filter = (
        'year',
    )
    search_fields = (
        'business__sector',
        'business__short_business_name',
        'business__full_business_name',
        'business__first_name',
        'business__last_name',
        'business__middle_name',
        'business__year',
        'business__address',
    )
    ordering = (
        'id',
        'business',
        'year',
    )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin[Report]):
    """Отчет."""

    list_display = (
        'id',
        'user',
    )
    search_fields = (
        'user__email',
        'user__first_name',
        'user_last_name',
    )
    ordering = (
        'id',
        'user',
    )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin[Equipment]):
    """Оборудование."""

    list_display = (
        'id',
        'name',
        'cost',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
        'name',
        'cost',
    )


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin[Sector]):
    """Сектор."""

    list_display = (
        'id',
        'name',
        'slug',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
        'name',
        'slug',
    )


@admin.register(SubSector)
class SubSectorAdmin(admin.ModelAdmin[SubSector]):
    """Сектор."""

    list_display = (
        'id',
        'name',
        'slug',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
        'name',
        'slug',
    )


@admin.register(TerritorialLocation)
class TerritorialLocationAdmin(admin.ModelAdmin[TerritorialLocation]):
    """Территориальное расположение."""

    list_display = (
        'id',
        'shot_name',
        'full_name',
        'slug',
    )
    search_fields = (
        'slug',
        'shot_name',
        'full_name',
    )
    ordering = (
        'id',
        'shot_name',
        'full_name',
        'slug',
    )


@admin.register(Statistic)
class StatisticnAdmin(admin.ModelAdmin[Statistic]):
    """Статистика"""

    list_display = (
        'id',
        'year',
        'sector',
        'volume_of_sales',
        'growth_rate',
    )
    list_filter = (
        'year',
        'sector',
    )
    search_fields = (
        'sector__name',
        'sector__slug'
        'year',
    )
    ordering = (
        'id',
        'year',
        'sector',
        'volume_of_sales',
        'growth_rate',
    )


