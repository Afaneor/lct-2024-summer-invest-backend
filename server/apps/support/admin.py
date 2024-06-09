from django.contrib import admin

from server.apps.support.models import (
    Problem,
    ProblemCategory,
    ProblemSubcategory,
    ProblemTheme,
    ServiceSupport,
)


@admin.register(ProblemCategory)
class ProblemCategoryAdmin(admin.ModelAdmin[ProblemCategory]):
    """Категория проблемы."""

    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
    )


@admin.register(ProblemSubcategory)
class ProblemCategoryAdmin(admin.ModelAdmin[ProblemSubcategory]):
    """Подкатегория проблемы."""

    list_display = (
        'id',
        'name',
        'problem_category',
    )
    list_filter = (
        'problem_category',
    )
    search_fields = (
        'name',
        'problem_category__name',
    )
    ordering = (
        'id',
    )


@admin.register(ProblemTheme)
class ProblemThemeAdmin(admin.ModelAdmin[ProblemTheme]):
    """Тема проблемы."""

    list_display = (
        'id',
        'name',
        'problem_subcategory',
    )
    list_filter = (
        'problem_subcategory',
    )
    search_fields = (
        'name',
        'problem_subcategory__name',
        'problem_subcategory__problem_category__name',
    )
    ordering = (
        'id',
    )


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin[Problem]):
    """Проблема."""

    list_display = (
        'id',
        'name',
        'problem_theme',
        'url',
    )
    list_filter = (
        'problem_theme',
        'problem_theme__problem_subcategory',
        'problem_theme__problem_subcategory__problem_category',
    )
    search_fields = (
        'name',
        'problem_theme__name',
        'problem_theme__problem_subcategory__name',
        'problem_theme__problem_subcategory__problem_category__name',
    )
    ordering = (
        'id',
    )


@admin.register(ServiceSupport)
class ServiceSupportAdmin(admin.ModelAdmin[ServiceSupport]):
    """Сервис поддержки."""

    list_display = (
        'id',
        'name',
        'service_support_type',
        'support_type',
        'support_level',
    )
    list_filter = (
        'service_support_type',
    )
    search_fields = (
        'name',
        'region',
    )
    ordering = (
        'id',
    )
