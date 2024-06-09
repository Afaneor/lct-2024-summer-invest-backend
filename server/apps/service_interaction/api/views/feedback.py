import django_filters

from server.apps.service_interaction.api.serializers import FeedbackSerializer, CreateFeedbackSerializer
from server.apps.service_interaction.models import Feedback
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin, \
    UserFilterMixin
from server.apps.services.views import RetrieveListCreateViewSet


class FeedbackFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр отзывов."""

    class Meta:
        model = Feedback
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
        )


class FeedbackViewSet(RetrieveListCreateViewSet):
    """Отзыв."""

    serializer_class = FeedbackSerializer
    create_serializer_class = CreateFeedbackSerializer
    queryset = Feedback.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = FeedbackFilter
