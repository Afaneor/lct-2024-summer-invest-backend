import abc

from llama_index.core.chat_engine.types import AgentChatResponse


class AbstractLLMProvider(abc.ABC):

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton pattern."""
        if not cls._instance:
            cls._instance = super(AbstractLLMProvider, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @abc.abstractmethod
    def chat(self, message: str) -> AgentChatResponse:
        pass

    @abc.abstractmethod
    def chat_no_rag(self, message: str) -> str:
        pass
