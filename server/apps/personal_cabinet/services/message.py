import json
from dataclasses import dataclass

from llama_index.core.chat_engine.types import AgentChatResponse
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

from server.apps.llm.providers.abstract import AbstractLLMProvider
from server.apps.llm.utils import get_llm_provider
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.personal_cabinet.models.message import Message
from server.apps.services.enums import MessageOwnerType


class MessageServiceException(APIException):
    status_code = 503
    default_detail = _('Нет возможности обработать сообщение в данный момент')
    default_code = 'message_service_error'


@dataclass
class LLMResponse:
    text: str
    bot_filter: dict | None = None


class MessageService(object):

    def __init__(
        self,
        llm_provider: AbstractLLMProvider | None = None,
    ):
        self.llm_provider = llm_provider
        if not self.llm_provider:
            self.llm_provider = get_llm_provider()

    def process_user_message(
        self,
        user_text: str,
        selection_request: SelectionRequest,
        message_id: int,
    ) -> Message:
        """Get response from LLM and create message."""
        selection_request.is_bot_response_waiting = True
        selection_request.save(
            update_fields=['is_bot_response_waiting'],
        )
        try:
            response = self._send_to_llm(user_text)
        except Exception:
            raise MessageServiceException

        try:
            response = LLMResponse(**json.loads(response.response))
        except json.JSONDecodeError:
            raise MessageServiceException

        message = Message.objects.create(
            owner_type=MessageOwnerType.ASSISTANT,
            selection_request=selection_request,
            text=response.text,
            bot_filter=response.bot_filter,
            parent_id=message_id,
        )

        selection_request.is_bot_response_waiting = False
        selection_request.save(
            update_fields=['is_bot_response_waiting'],
        )
        return message

    def _send_to_llm(
        self,
        user_text: str,
    ) -> AgentChatResponse:
        """
        Отправляем информацию в LLM.
        """
        return self.llm_provider.chat(user_text)

