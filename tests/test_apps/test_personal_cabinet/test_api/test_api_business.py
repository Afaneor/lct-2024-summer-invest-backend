import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from server.apps.services.enums import BusinessType
from tests.test_apps.conftest import object_without_keys


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
    user_api_client,
    user,
):
    """Создание Business."""
    url = reverse('api:personal-cabinet:businesses-list')
    response = user_api_client.post(
        url,
        data={
            'user': user.id,
            'business_type': BusinessType.LEGAL,
            'inn': '7707083893',
            'full_business_name': 'ООО Ромашка',

        },
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_business_create_by_inn_without_access(
    user_api_client,
    user,
):
    """Создание Business."""
    url = reverse('api:personal-cabinet:businesses-create-business-by-inn')
    response = user_api_client.post(
        url,
        data={
            'inn': '7707083893',
        },
        format='json',
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert (
        response.json()['detail'] ==
        (
            'При добавлении по ИНН вашего бизнеса произошла '
            'ошибка, связанная с доступом к сервису DaData.'
            'Вы можете добавить информацию в ручную.'
        )
    )


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
