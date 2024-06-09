import django_filters

from server.apps.service_interaction.api.serializers import (
    CommentSerializer,
    CreateCommentSerializer,
)
from server.apps.service_interaction.models import Comment
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateViewSet


class CommentFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр отзывов."""

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'content_type',
            'object_id',
        )


class CommentViewSet(RetrieveListCreateViewSet):
    """Комментарий."""

    serializer_class = CommentSerializer
    create_serializer_class = CreateCommentSerializer
    queryset = Comment.objects.select_related('user')
    search_fields = (
        'text',
    )
    ordering_fields = '__all__'
    filterset_class = CommentFilter
