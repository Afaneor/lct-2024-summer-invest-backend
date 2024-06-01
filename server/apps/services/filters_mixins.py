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

    start_created_at = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='gte',
    )
    end_created_at = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='lte',
    )
    start_updated_at = django_filters.DateTimeFilter(
        field_name='updated_at',
        lookup_expr='gte',
    )
    end_updated_at = django_filters.DateTimeFilter(
        field_name='updated_at',
        lookup_expr='lte',
    )
    range_created_at = NonValidatingMultipleChoiceFilter(
        method='range_created_at_filter',
    )
    range_updated_at = NonValidatingMultipleChoiceFilter(
        method='range_updated_at_filter',
    )

    def range_created_at_filter(self, queryset, name, date_value):
        """Фильтруем объект по дате создания."""
        if len(date_value) == 2:
            return queryset.filter(
                created_at__gte=date_value[0],
                created_at__lte=date_value[1],
            )
        return queryset

    def range_updated_at_filter(self, queryset, name, date_value):
        """Фильтруем объект по дате изменения."""
        if len(date_value) == 2:
            return queryset.filter(
                updated_at__gte=date_value[0],
                updated_at__lte=date_value[1],
            )
        return queryset


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
