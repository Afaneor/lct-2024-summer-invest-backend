import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_tender_lot_format(
    api_client,
    tender_lot,
    tender_lot_format,
):
    """Формат TenderLot."""
    url = reverse('investment-object:tender-lot-detail', [tender_lot.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == tender_lot_format(tender_lot)


@pytest.mark.django_db()
def test_tender_lot_post(
    api_client,
):
    """Создание TenderLot."""
    url = reverse('investment-object:tender-lot-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_tender_lot_delete(api_client, tender_lot):
    """Удаление TenderLot."""
    url = reverse('investment-object:tender-lot-detail', [tender_lot.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_tender_lot_change(
    api_client,
    tender_lot,
):
    """Изменение TenderLot."""
    url = reverse('api:investment-object:tender-lot-detail', [tender_lot.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
