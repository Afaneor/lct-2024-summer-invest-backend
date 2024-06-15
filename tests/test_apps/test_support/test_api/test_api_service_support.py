import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_service_support_detail(
    api_client,
    service_support,
    service_support_format,
):
    """Формат ServiceSupport."""
    url = reverse('api:support:service-supports-detail', [service_support.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        service_support_format(service_support)
    )


@pytest.mark.django_db()
def test_service_support_list(
    api_client,
):
    """Список ServiceSupport."""
    url = reverse('api:support:service-supports-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
