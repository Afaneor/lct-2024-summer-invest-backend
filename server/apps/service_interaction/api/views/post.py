import django_filters

from server.apps.service_interaction.api.serializers import (
    CreatePostSerializer,
    PostSerializer,
)
from server.apps.service_interaction.models import Post
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateViewSet


class PostFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр постов."""

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'topic',
            'parent',
        )


class PostViewSet(RetrieveListCreateViewSet):
    """Пост."""

    serializer_class = PostSerializer
    create_serializer_class = CreatePostSerializer
    queryset = Post.objects.select_related('user', 'topic')
    ordering_fields = '__all__'
    filterset_class = PostFilter
