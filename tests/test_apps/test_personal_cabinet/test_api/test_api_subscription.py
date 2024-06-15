import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from server.apps.services.enums import SubscriptionType
from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_subscription_detail(
    user_api_client,
    subscription,
    subscription_format,
):
    """Формат Subscription."""
    url = reverse(
        'api:personal-cabinet:subscriptions-detail',
        [subscription.id],
    )

    response = user_api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        subscription_format(subscription)
    )


@pytest.mark.django_db()
def test_subscription_post(
    user_api_client,
):
    """Создание Subscription."""
    url = reverse('api:personal-cabinet:subscriptions-list')

    response = user_api_client.post(
        url,
        data={
            'subscription_type': SubscriptionType.EVENT,
            'email': 'test@test.ru',
            'telegram_username': '@test',
        },
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_subscription_delete(user_api_client, subscription):
    """Удаление Subscription."""
    url = reverse(
        'api:personal-cabinet:subscriptions-detail',
        [subscription.id],
    )

    response = user_api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_subscription_list(
    user_api_client,
    subscription,
):
    """Список Subscription."""
    url = reverse(
        'api:personal-cabinet:subscriptions-detail',
        [subscription.id],
    )

    response = user_api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
