from datetime import timedelta

import openai
from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import now

from server.apps.investment_object.models import InvestmentObject
from server.apps.personal_cabinet.models import Subscription
from server.apps.personal_cabinet.services.create_business import (
    update_or_create_business,
)
from server.apps.service_interaction.models.event import Event
from server.apps.service_interaction.models.post import Post
from server.apps.services.enums import SubscriptionType
from server.apps.support.models import ServiceSupport
from server.celery import app


@app.task(bind=True)
def delayed_create_business(self, inn: str, user_id: int) -> None:
    """Выбираем нужную информацию о компании или ИП и сохраняем ее в БД.

    Информация берется из DaData.
    """
    update_or_create_business(
        inn=inn,
        user_id=user_id,
    )


# @app.task(bind=True)
# def send_info_in_chat_gpt(self, sector: str, report_id: int) -> None:
#     openai.api_key = settings.OPENAI_API_KEY
#
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=[
#             {
#                 'role': 'user',
#                 'content': 'test'
#             },
#         ],
#         temperature=0.7,
#         top_p=1.0,
#         n=1,
#         max_tokens=2048,
#     )
#     answers = response.choices[0].message.content


@app.task(
    name='send_data_to_the_user_by_subscription_on_email',
)
def send_data_to_the_user_by_subscription_on_email() -> None:
    """Отправлять данные пользователю по подписке на почту."""
    # Получаем пользователей у которых есть подписка.
    subscription_investment_object_user = Subscription.objects.filter(
        subscription_type=SubscriptionType.INVESTMENT_OBJECT,
    ).values_list('email', flat=True)
    subscription_service_support_user = Subscription.objects.filter(
        subscription_type=SubscriptionType.SERVICE_SUPPORT,
    ).values_list('email', flat=True)
    subscription_topic_user = Subscription.objects.filter(
        subscription_type=SubscriptionType.TOPIC,
    ).values_list('email', flat=True)
    subscription_event_user = Subscription.objects.filter(
        subscription_type=SubscriptionType.EVENT,
    ).values_list('email', flat=True)

    # Формируем объекты, которые были добавлены за последние
    # SEND_DATA_TO_THE_USER_BY_SUBSCRIPTION_MINUTE минут.
    now_datetime = now()
    investment_objects = InvestmentObject.objects.filter(
        created_at__gte=now_datetime - timedelta(
            minutes=settings.SEND_DATA_TO_THE_USER_BY_SUBSCRIPTION_MINUTE,
        ),
        created_at__lte=now_datetime,
    ).values_list('id', 'name')
    service_supports = ServiceSupport.objects.filter(
        created_at__gte=now_datetime - timedelta(
            minutes=settings.SEND_DATA_TO_THE_USER_BY_SUBSCRIPTION_MINUTE,
        ),
        created_at__lte=now_datetime,
    ).values_list('id', 'name')
    topics = Post.objects.filter(
        created_at__gte=now_datetime - timedelta(
            minutes=settings.SEND_DATA_TO_THE_USER_BY_SUBSCRIPTION_MINUTE,
        ),
        created_at__lte=now_datetime,
    ).values_list('post__topic__id', 'post__topic__name')
    events = Event.objects.filter(
        created_at__gte=now_datetime - timedelta(
            minutes=settings.SEND_DATA_TO_THE_USER_BY_SUBSCRIPTION_MINUTE,
        ),
        created_at__lte=now_datetime,
    ).values_list('id', 'name', 'event_datetime', flat=True)

    # Проверяем были ли добавлены объекты. Если были, то отправляем
    # информацию о них.
    if investment_objects:
        message = ''
        for index, investment_object in enumerate(investment_objects):
            message += (
                f'{index}) {investment_object[1]}. {investment_object[0]}.'
            )
        send_mail(
            subject=_('Новый инвестиционный объект!'),  # type: ignore
            message=(
                'Быстрее ознакомьтесь с новыми объектами для инвестирования!\n'
                f'{message}'
            ),
            from_email=None,
            recipient_list=list(subscription_investment_object_user),
        )

    if service_supports:
        message = ''
        for index, service_support in enumerate(service_supports):
            message += (
                f'{index}) {service_support[1]}. {service_support[0]}.'
            )
        send_mail(
            subject=_('Новые меры поддержки!'),  # type: ignore
            message=(
                'Быстрее ознакомьтесь с новыми мерами поддержки!\n'
                f'{message}'
            ),
            from_email=None,
            recipient_list=list(subscription_service_support_user),
        )

    # FIXME: Дописать логику на проверку нужно ли отслеживать топик
    #  для пользователя или нет.
    if topics:
        message = ''
        for index, topic in enumerate(topics):
            message += (
                f'{index}) {topic[1]}.'
            )
        send_mail(
            subject=_('Новые сообщения в темах!'),  # type: ignore
            message=(
                'Быстрее ознакомьтесь с новыми сообщения в темах!\n'
                f'{message}'
            ),
            from_email=None,
            recipient_list=list(subscription_topic_user),
        )

    if events:
        message = ''
        for index, event in enumerate(events):
            message += (
                f'{index}) {event[1]}. Время проведения: {event[2]}'
            )
        send_mail(
            subject=_('Новые события!'),  # type: ignore
            message=(
                'Быстрее ознакомьтесь с новыми событиями!\n'
                f'{message}'
            ),
            from_email=None,
            recipient_list=list(subscription_event_user),
        )


@app.task(
    name='send_data_to_the_user_by_subscription_on_telegram',
)
def send_data_to_the_user_by_subscription_on_telegram() -> None:
    """Отправлять данные пользователю по подписке в телеграм."""
    pass
