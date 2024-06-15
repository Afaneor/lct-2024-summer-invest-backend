import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_business_detail(
    user_api_client,
    business,
    business_format,
):
    """Формат Business."""
    url = reverse('api:personal-cabinet:businesses-detail', [business.id])

    response = user_api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        business_format(business)
    )


@pytest.mark.django_db()
def test_business_post(
    api_client,
):
    """Создание Business."""
    url = reverse('api:personal-cabinet:business-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_business_delete(user_api_client, business):
    """Удаление Business."""
    url = reverse('api:personal-cabinet:businesses-detail', [business.id])

    response = user_api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_business_change(
    user_api_client,
    business,
):
    """Изменение Business."""
    url = reverse('api:personal-cabinet:businesses-detail', [business.id])

    response = user_api_client.patch(
        url,
        data={
            'full_opf': 'ООО ТЕСТ'
        },
        format='json',
    )
    business.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert business.full_opf == 'ООО ТЕСТ'
