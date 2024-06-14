import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import response_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_investment_object_detail(
    api_client,
    investment_object,
    investment_object_format,
):
    """Формат InvestmentObject."""
    url = reverse(
        'api:investment-object:investment-objects-detail',
        [investment_object.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        response_without_keys(response.json()) ==
        investment_object_format(investment_object)
    )


@pytest.mark.django_db()
def test_investment_object_list(
    api_client,
):
    """Создание InvestmentObject."""
    url = reverse('api:investment-object:investment-objects-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
