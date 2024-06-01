import django_filters

from server.apps.blog.api.serializers import PostSerializer
from server.apps.blog.models import Post
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    TagFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet


class PostFilter(
    TagFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр записей."""

    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Post
        fields = (
            'title',
            'tags',
            'is_published',
        )


class PostViewSet(BaseReadOnlyViewSet):
    """Посты. Просмотр."""

    serializer_class = PostSerializer
    queryset = Post.objects.prefetch_related('tags')
    ordering_fields = '__all__'
    search_fields = ('title',)
    filterset_class = PostFilter

    def get_queryset(self):  # noqa: WPS615
        """Выдача постов.

        Суперпользователь видит все.
        Остальные видят только опубликованные посты.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        return queryset.filter(is_published=True)
