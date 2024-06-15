import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_ready_business_detail(
    api_client,
    ready_business,
    ready_business_format,
):
    """Формат ReadyBusiness."""
    url = reverse(
        'api:investment-object:ready-businesses-detail',
        [ready_business.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        ready_business_format(ready_business)
    )


@pytest.mark.django_db()
def test_ready_business_list(
    api_client,
):
    """Список ReadyBusiness."""
    url = reverse('api:investment-object:ready-businesses-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
