from llama_index.core.chat_engine.types import AgentChatResponse

from server.apps.llm.providers.abstract import AbstractLLMProvider


class DummyProvider(AbstractLLMProvider):

    def chat(self, message: str, response=None) -> AgentChatResponse:
        response = response or f'Response to "{message}" from DummyProvider.'
        return AgentChatResponse(response=response)
