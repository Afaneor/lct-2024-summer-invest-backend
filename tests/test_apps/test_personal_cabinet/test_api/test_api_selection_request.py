import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_selection_request_format(
    api_client,
    selection_request,
    selection_request_format,
):
    """Формат SelectionRequest."""
    url = reverse('personal-cabinet:selection-request-detail', [selection_request.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == selection_request_format(selection_request)


@pytest.mark.django_db()
def test_selection_request_post(
    api_client,
):
    """Создание SelectionRequest."""
    url = reverse('personal-cabinet:selection-request-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_selection_request_delete(api_client, selection_request):
    """Удаление SelectionRequest."""
    url = reverse('personal-cabinet:selection-request-detail', [selection_request.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_selection_request_change(
    api_client,
    selection_request,
):
    """Изменение SelectionRequest."""
    url = reverse('api:personal-cabinet:selection-request-detail', [selection_request.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
