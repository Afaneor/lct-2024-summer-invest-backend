from django.contrib import admin

from server.apps.support.models import ServiceProblem, ServiceSupport


@admin.register(ServiceProblem)
class ServiceProblemAdmin(admin.ModelAdmin[ServiceProblem]):
    """Сообщение о проблеме."""

    list_display = (
        'id',
        'name',
        'category_name',
        'subcategory_name',
        'theme_name',
    )
    list_filter = (
        'category_name',
        'subcategory_name',
        'theme_name',
    )
    search_fields = (
        'name',
        'category_name',
        'subcategory_name',
        'theme_name',
    )
    ordering = (
        'id',
    )


admin.site.register(ServiceSupport)
