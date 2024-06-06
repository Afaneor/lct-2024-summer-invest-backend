from typing import List, Optional

import django_filters
from django.db import models
from django_filters.fields import MultipleChoiceField


class NonValidatingMultipleChoiceField(MultipleChoiceField):
    """Поле для множественного выбора данных без валидации."""

    def validate(self, value):  # noqa: WPS110
        """Отключение валидации, чтобы можно было передавать любые значения."""
        pass  # noqa: WPS420


class NonValidatingMultipleChoiceFilter(django_filters.MultipleChoiceFilter):
    """Фильтр для множественного выбора данных без валидации."""

    field_class = NonValidatingMultipleChoiceField


class TagFilterMixin(django_filters.FilterSet):
    """Миксин для фильтрации по тегам."""

    tags = django_filters.CharFilter(method='tags_filter')

    def tags_filter(self, queryset, name, tags_value):
        """Фильтруем объект по тегам."""
        filtered_queryset = queryset.filter(
            tags__name__in=tags_value.split(','),
        )
        if not filtered_queryset:
            return self.Meta.model.objects.none()
        return filtered_queryset


class CreatedUpdatedDateFilterMixin(django_filters.FilterSet):
    """Миксин для фильтрации по датам создания и обновления."""

    created_at_date = django_filters.DateFromToRangeFilter(
        field_name='created_at__date',
    )

    updated_at_date = django_filters.DateFromToRangeFilter(
        field_name='updated_at__date',
    )


class CurrentStageFilterMixin(django_filters.FilterSet):
    """Миксин для фильтрации по current_stage."""

    current_stage_name = django_filters.CharFilter(
        method='filter_current_stage_name',
    )
    current_stage_type = django_filters.CharFilter(
        field_name='current_stage__type',
    )

    def filter_current_stage_name(self, queryset, name, value_name):
        """Фильтруем этап по имени."""
        return queryset.filter(
            models.Q(current_stage__name=value_name) |
            models.Q(current_stage__plural_name=value_name),
        )


class UserFilterMixin(django_filters.FilterSet):
    """Миксин для фильтрации по пользователю."""

    user_email = django_filters.CharFilter(
        field_name='user__email',
        lookup_expr='icontains',
    )
    user_username = django_filters.CharFilter(
        field_name='user__username',
        lookup_expr='icontains',
    )
    user_first_name = django_filters.CharFilter(
        field_name='user__first_name',
        lookup_expr='icontains',
    )
    user_last_name = django_filters.CharFilter(
        field_name='user__last_name',
        lookup_expr='icontains',
    )
    user_middle_name = django_filters.CharFilter(
        field_name='user__middle_name',
        lookup_expr='icontains',
    )


def get_companies_query(  # noqa: WPS234
    companies_id: Optional[List[str]],
    flag: str,
):
    """Получение фильтра для компаний, переданных в запросе."""
    if companies_id:
        if flag in {'asset', 'leak', 'phishing_resource'}:
            return models.Q(company_id__in=companies_id)
        if flag == 'service':
            return models.Q(asset__company_id__in=companies_id)
        if flag == 'vulnerability':
            return models.Q(service__asset__company_id__in=companies_id)
        if flag == 'stage':
            return models.Q(process__company_id__in=companies_id)

    return models.Q()
