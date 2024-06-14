import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import response_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_economic_activity_detail(
    api_client,
    economic_activity,
    economic_activity_format,
):
    """Формат EconomicActivity."""
    url = reverse(
        'api:investment-object:economic-activities-detail',
        [economic_activity.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        response_without_keys(response.json()) ==
        economic_activity_format(economic_activity)
    )


@pytest.mark.django_db()
def test_economic_activity_list(
    api_client,
):
    """Формат EconomicActivity."""
    url = reverse(
        'api:investment-object:economic-activities-list',
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
