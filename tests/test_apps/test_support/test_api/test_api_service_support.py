import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_service_support_format(
    api_client,
    service_support,
    service_support_format,
):
    """Формат ServiceSupport."""
    url = reverse('support:service-support-detail', [service_support.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == service_support_format(service_support)


@pytest.mark.django_db()
def test_service_support_post(
    api_client,
):
    """Создание ServiceSupport."""
    url = reverse('support:service-support-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_service_support_delete(api_client, service_support):
    """Удаление ServiceSupport."""
    url = reverse('support:service-support-detail', [service_support.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_service_support_change(
    api_client,
    service_support,
):
    """Изменение ServiceSupport."""
    url = reverse('api:support:service-support-detail', [service_support.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
