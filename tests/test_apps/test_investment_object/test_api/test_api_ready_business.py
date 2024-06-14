import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_ready_business_format(
    api_client,
    ready_business,
    ready_business_format,
):
    """Формат ReadyBusiness."""
    url = reverse('investment-object:ready-business-detail', [ready_business.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == ready_business_format(ready_business)


@pytest.mark.django_db()
def test_ready_business_post(
    api_client,
):
    """Создание ReadyBusiness."""
    url = reverse('investment-object:ready-business-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_ready_business_delete(api_client, ready_business):
    """Удаление ReadyBusiness."""
    url = reverse('investment-object:ready-business-detail', [ready_business.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_ready_business_change(
    api_client,
    ready_business,
):
    """Изменение ReadyBusiness."""
    url = reverse('api:investment-object:ready-business-detail', [ready_business.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
