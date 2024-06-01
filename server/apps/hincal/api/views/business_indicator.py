import django_filters

from server.apps.hincal.api.serializers import BusinessIndicatorSerializer
from server.apps.hincal.models import BusinessIndicator
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseModelViewSet


class BusinessIndicatorFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр показателей бизнеса."""

    class Meta(object):
        model = BusinessIndicator
        fields = (
            'id',
            'business',
            'year',
        )


class BusinessIndicatorViewSet(BaseModelViewSet):
    """Экономические показатели ИП, физического лица или компании."""

    serializer_class = BusinessIndicatorSerializer
    queryset = BusinessIndicator.objects.select_related('business')
    search_fields = (
        'business__short_business_name',
        'business__sector',
    )
    ordering_fields = '__all__'
    filterset_class = BusinessIndicatorFilter

    def get_queryset(self):
        """Выдача экономических показателей.

        Суперпользователь видит все показатели.
        Остальные видят показатели в рамках своего бизнеса.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        if user.is_anonymous:
            return queryset.none()

        return queryset.filter(
            business__in=user.businesses.all()
        )
