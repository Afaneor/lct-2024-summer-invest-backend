import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_selection_request_format(
    api_client,
    selection_request,
    selection_request_format,
):
    """Формат SelectionRequest."""
    url = reverse(
        'api:personal-cabinet:selection-requests-detail',
        [selection_request.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        selection_request_format(selection_request)
    )


@pytest.mark.django_db()
def test_selection_request_post(
    api_client,
):
    """Создание SelectionRequest."""
    url = reverse('api:personal-cabinet:selection-requests-list')
    response = api_client.post(
        url,
        data={
            'anonymous_user_id': 'test-anonymous-user-id',
        },
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_selection_request_list(
    api_client,
):
    """Список SelectionRequest."""
    url = reverse(
        'api:personal-cabinet:selection-requests-list',
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
