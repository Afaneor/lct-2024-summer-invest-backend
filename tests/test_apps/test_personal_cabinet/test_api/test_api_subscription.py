import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_subscription_format(
    api_client,
    subscription,
    subscription_format,
):
    """Формат Subscription."""
    url = reverse('personal-cabinet:subscription-detail', [subscription.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == subscription_format(subscription)


@pytest.mark.django_db()
def test_subscription_post(
    api_client,
):
    """Создание Subscription."""
    url = reverse('personal-cabinet:subscription-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_subscription_delete(api_client, subscription):
    """Удаление Subscription."""
    url = reverse('personal-cabinet:subscription-detail', [subscription.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_subscription_change(
    api_client,
    subscription,
):
    """Изменение Subscription."""
    url = reverse('api:personal-cabinet:subscription-detail', [subscription.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
