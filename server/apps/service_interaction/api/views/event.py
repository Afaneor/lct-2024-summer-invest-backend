import django_filters

from server.apps.service_interaction.api.serializers import (
    DetailEventSerializer,
    ListEventSerializer,
)
from server.apps.service_interaction.models import Event
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class EventFilter(
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


class EventViewSet(RetrieveListViewSet):
    """Событие."""

    serializer_class = DetailEventSerializer
    list_serializer_class = ListEventSerializer
    queryset = Event.objects.all()
    search_fields = (
        'name',
        'shot_description',
    )
    ordering_fields = '__all__'
    filterset_class = EventFilter
