from django.conf import settings
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.chat_engine import ContextChatEngine
from llama_index.llms.ollama import Ollama

from server.apps.llm.providers.abstract import AbstractLLMProvider


class LocalProvider(AbstractLLMProvider):
    def __init__(self):
        self.llm = Ollama(model='llama3', base_url=settings.OLLAMA_HOST)
        index = VectorStoreIndex.from_documents(self.__load_data())
        self.engine = ContextChatEngine.from_defaults(
            llm=self.llm,
            retriever=index.as_retriever(),
        )

    def __load_data(self):
        documents_directory = settings.BASE_DIR / 'data'
        documents = SimpleDirectoryReader(documents_directory).load_data()
        return documents

    def chat(self, message: str):
        self.engine.chat()