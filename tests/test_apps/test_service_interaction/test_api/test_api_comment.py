import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_comment_format(
    api_client,
    comment,
    comment_format,
):
    """Формат Comment."""
    url = reverse('api:service-interaction:comments-detail', [comment.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        comment_format(comment)
    )


@pytest.mark.django_db()
def test_comment_post(
    user_api_client,
    investment_object,
):
    """Создание Comment."""
    url = reverse('api:service-interaction:comments-list')
    response = user_api_client.post(
        url,
        data={
            'text': 'тест',
            'content_type': investment_object.content_type_id,
            'object_id': investment_object.id,
        },
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_comment_list(api_client, comment):
    """Удаление Comment."""
    url = reverse('api:service-interaction:comments-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
