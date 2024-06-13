from django.conf import settings
from llama_index.agent.openai import OpenAIAssistantAgent
from llama_index.core.chat_engine.types import AgentChatResponse

from server.apps.llm.providers.abstract import AbstractLLMProvider


class GPTProvider(AbstractLLMProvider):

    def __init__(self):
        self.engine = OpenAIAssistantAgent.from_existing(
            assistant_id=settings.OPENAI_ASSISTANT_ID,
            api_key=settings.OPENAI_API_KEY,
        )

    def chat(self, message: str) -> AgentChatResponse:
        return self.engine.chat(message)
