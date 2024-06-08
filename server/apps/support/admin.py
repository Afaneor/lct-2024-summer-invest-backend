from django.contrib import admin

from server.apps.support.models import Problem, ServiceSupport, ProblemTheme, \
    ProblemSubcategory, ProblemCategory


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin[Problem]):
    """Сообщение о проблеме."""

    list_display = (
        'id',
        'name',
    )
    # list_filter = (
    #     'problem_theme',
    # )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
    )


admin.site.register(ProblemCategory)
admin.site.register(ProblemSubcategory)
admin.site.register(ProblemTheme)
admin.site.register(ServiceSupport)
