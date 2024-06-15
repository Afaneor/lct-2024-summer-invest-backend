import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_problem_category_detail(
    api_client,
    problem_category,
    problem_category_format,
):
    """Формат ProblemCategory."""
    url = reverse(
        'api:support:problem-categories-detail',
        [problem_category.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        problem_category_format(problem_category)
    )


@pytest.mark.django_db()
def test_problem_category_list(
    api_client,
):
    """Список ProblemCategory."""
    url = reverse('api:support:problem-categories-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
