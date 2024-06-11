import django_filters
from django.utils.translation import gettext_lazy as _

from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    NonValidatingMultipleChoiceFilter,
)
from server.apps.services.views import RetrieveListViewSet
from server.apps.support.api.serializers import ProblemCategorySerializer
from server.apps.support.models import ProblemCategory


class ProblemCategoryFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инфраструктуры."""

    problem_subcategory_id = NonValidatingMultipleChoiceFilter(
        field_name='problem_subcategories__name',
        label=_('Фильтр по id подкатегории проблемы')
    )
    problem_subcategory_name = NonValidatingMultipleChoiceFilter(
        field_name='problem_subcategories__name',
        label=_('Фильтр по названиям подкатегории проблемы')
    )
    problem_theme_id = NonValidatingMultipleChoiceFilter(
        field_name='problem_subcategories__problem_themes__id',
        label=_('Фильтр по id темы проблемы')
    )
    problem_theme_name = NonValidatingMultipleChoiceFilter(
        field_name='problem_subcategories__problem_themes__name',
        label=_('Фильтр по названиям темы проблемы')
    )
    problem_id = NonValidatingMultipleChoiceFilter(
        field_name='problem_subcategories__problem_themes__problems__id',
        label=_('Фильтр по названию проблем')
    )
    problem_name = NonValidatingMultipleChoiceFilter(
        field_name='problem_subcategories__problem_themes__problems__name',
        label=_('Фильтр по id проблем')
    )

    class Meta:
        model = ProblemCategory
        fields = (
            'id',
            'name',
            'problem_subcategory_id',
            'problem_subcategory_name',
            'problem_theme_name',
            'problem_theme_id',
            'problem_name',
            'problem_id',
        )


class ProblemCategoryViewSet(RetrieveListViewSet):
    """Инфраструктура."""

    serializer_class = ProblemCategorySerializer
    queryset = ProblemCategory.objects.all()
    search_fields = (
        'name',
        'problem_subcategories__name',
        'problem_subcategories__problem_themes__name',
        'problem_subcategories__problem_themes__problems__name',
    )
    ordering_fields = '__all__'
    filterset_class = ProblemCategoryFilter
