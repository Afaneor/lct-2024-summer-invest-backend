import django_filters

from server.apps.service_interaction.api.serializers import (
    DetailTopicSerializer,
    ListTopicSerializer,
)
from server.apps.service_interaction.models import Topic
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class TopicFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр темы."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
        )


class TopicViewSet(RetrieveListViewSet):
    """Тема."""

    serializer_class = DetailTopicSerializer
    list_serializer_class = ListTopicSerializer
    queryset = Topic.objects.all().prefetch_related('posts')
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = TopicFilter
