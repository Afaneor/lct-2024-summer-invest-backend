from django.contrib import admin

from server.apps.service_interaction.models import Comment
from server.apps.service_interaction.models.event import Event
from server.apps.service_interaction.models.post import Post
from server.apps.service_interaction.models.topic import Topic


@admin.register(Event)
class EventAdmin(admin.ModelAdmin[Event]):
    """Событие."""

    list_display = (
        'id',
        'name',
        'event_datetime',
        'event_type',
    )
    list_filter = (
        'event_type',
    )
    search_fields = (
        'name',
    )
    ordering = (
        '-id',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin[Comment]):
    """Комментарий."""

    list_display = (
        'id',
        'user',
        'text',
    )
    search_fields = (
        'name',
    )
    ordering = (
        '-id',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin[Post]):
    """Пост."""

    list_display = (
        'id',
        'user',
        'topic',
        'parent',
    )
    list_filter = (
        'topic',
    )
    search_fields = (
        'topic__name',
    )
    ordering = (
        '-id',
    )


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin[Topic]):
    """тема."""

    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    ordering = (
        '-id',
    )
