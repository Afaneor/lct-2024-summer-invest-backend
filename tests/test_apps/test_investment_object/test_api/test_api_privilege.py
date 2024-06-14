import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import response_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_privilege_detail(
    api_client,
    privilege,
    privilege_format,
):
    """Формат Privilege."""
    url = reverse('api:investment-object:privileges-detail', [privilege.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        response_without_keys(response.json()) ==
        privilege_format(privilege)
    )


@pytest.mark.django_db()
def test_privilege_list(
    api_client,
):
    """Список Infrastructure."""
    url = reverse('api:investment-object:privileges-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
