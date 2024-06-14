import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_business_format(
    api_client,
    business,
    business_format,
):
    """Формат Business."""
    url = reverse('personal-cabinet:business-detail', [business.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == business_format(business)


@pytest.mark.django_db()
def test_business_post(
    api_client,
):
    """Создание Business."""
    url = reverse('personal-cabinet:business-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_business_delete(api_client, business):
    """Удаление Business."""
    url = reverse('personal-cabinet:business-detail', [business.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_business_change(
    api_client,
    business,
):
    """Изменение Business."""
    url = reverse('api:personal-cabinet:business-detail', [business.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
