from django.conf import settings
from llama_index.agent.openai import OpenAIAssistantAgent

from server.apps.llm.providers.abstract import AbstractLLMProvider


class GPTProvider(AbstractLLMProvider):

    def __init__(self):
        self.engine = OpenAIAssistantAgent.from_existing(
            assistant_id=settings.OPENAI_ASSISTANT_ID,
            api_key=settings.OPENAI_API_KEY,
        )

    def chat(self, message: str):
        return self.engine.chat()
