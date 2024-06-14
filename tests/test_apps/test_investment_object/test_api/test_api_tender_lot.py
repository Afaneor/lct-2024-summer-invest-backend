import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import response_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_tender_lot_format(
    api_client,
    tender_lot,
    tender_lot_format,
):
    """Формат TenderLot."""
    url = reverse('api:investment-object:tender-lots-detail', [tender_lot.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        response_without_keys(response.json()) ==
        tender_lot_format(tender_lot)
    )


@pytest.mark.django_db()
def test_tender_lot_list(
    api_client,
):
    """Список TenderLot."""
    url = reverse('api:investment-object:tender-lots-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
