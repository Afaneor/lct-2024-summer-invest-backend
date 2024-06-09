import django_filters

from server.apps.service_interaction.api.serializers import (
    DetailTopicSerializer,
    ListTopicSerializer,
)
from server.apps.service_interaction.models import Topic
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListCreateViewSet


class TopicFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр постов."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
        )


class TopicViewSet(RetrieveListCreateViewSet):
    """Пост."""

    serializer_class = DetailTopicSerializer
    list_serializer_class = ListTopicSerializer
    queryset = Topic.objects.all().prefetch_related('posts')
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = TopicFilter
