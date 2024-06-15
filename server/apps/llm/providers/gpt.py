from django.conf import settings
from llama_index.agent.openai import OpenAIAssistantAgent
from llama_index.core.base.llms.types import ChatResponse
from llama_index.core.chat_engine.types import AgentChatResponse
from llama_index.llms.openai import OpenAI
from llama_index_client import ChatMessage

from server.apps.llm.providers.abstract import AbstractLLMProvider


class GPTProvider(AbstractLLMProvider):

    def __init__(self):
        self.engine = OpenAIAssistantAgent.from_existing(
            assistant_id=settings.OPENAI_ASSISTANT_ID,
            api_key=settings.OPENAI_API_KEY,
        )
        self.no_rag = OpenAI(model='gpt-4o', api_key=settings.OPENAI_API_KEY)

    def chat(self, message: str) -> AgentChatResponse:
        return self.engine.chat(message)

    def chat_no_rag(self, message: str) -> str:
        messages = [ChatMessage(content=message, role='user', additional_kwargs={})]
        return self.no_rag.chat(messages).message.content

    @property
    def system_prompt(self) -> str:
        """
        Prompt is fixed in chatGPT assistant.

        :return: str
        """
        return settings.SYSTEM_PROMPT
