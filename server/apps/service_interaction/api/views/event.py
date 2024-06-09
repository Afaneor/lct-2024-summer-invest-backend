import django_filters

from server.apps.service_interaction.api.serializers import (
    DetailEventSerializer,
    ListEventSerializer,
)
from server.apps.service_interaction.models import Event
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateViewSet


class EventFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр событий."""

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'event_datetime',
            'event_type',
        )


class EventViewSet(RetrieveListCreateViewSet):
    """Событие."""

    serializer_class = DetailEventSerializer
    list_serializer_class = ListEventSerializer
    queryset = Event.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = EventFilter
