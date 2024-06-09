import django_filters

from server.apps.service_interaction.api.serializers import TopicSerializer
from server.apps.service_interaction.models import Topic
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin, \
    UserFilterMixin
from server.apps.services.views import RetrieveListCreateViewSet


class TopicFilter(
    UserFilterMixin,
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

    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    ordering_fields = '__all__'
    filterset_class = TopicFilter
