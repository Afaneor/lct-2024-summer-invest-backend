from django.contrib import admin

from server.apps.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin[Post]):
    """Класс админки постов."""

    list_display = (
        'id',
        'title',
        'is_published',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'is_published',
    )
    ordering = (
        'id',
        'title',
        'is_published',
    )
