import pytest
from model_bakery import baker
from rest_framework.reverse import reverse

from server.apps.llm.providers.dummy import DummyProvider
from server.apps.llm.utils import get_llm_provider
from server.apps.personal_cabinet.models.message import Message


def test_get_llm_provider(settings, mocker):
    settings.LLM_PROVIDER = 'server.apps.llm.providers.dummy.DummyProvider'
    settings.OPENAI_ASSISTANT_ID = 'test'
    mocker.patch('server.apps.llm.providers.gpt.OpenAIAssistantAgent')
    provider = get_llm_provider()
    assert isinstance(provider, DummyProvider)


@pytest.mark.django_db
def test_create_message(settings, api_client):
    settings.LLM_PROVIDER = 'server.apps.llm.providers.dummy.DummyProvider'
    selection_request = baker.make('personal_cabinet.SelectionRequest')
    response = api_client.post(
        reverse('api:personal-cabinet:messages-list'),
        {'text': 'test', 'selection_request': selection_request.id},
    )
    assert response.status_code == 201
    assert Message.objects.count() == 2

