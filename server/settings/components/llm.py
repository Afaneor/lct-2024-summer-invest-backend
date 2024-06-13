from decouple import config

LLM_PROVIDER = config('LLM_PROVIDER', default='server.apps.llm.providers.GPTProvider')
OPENAI_ASSISTANT_ID = config('OPENAI_ASSISTANT_ID', '')
OLLAMA_HOST = config('OLLAMA_HOST', default='http://localhost:11434')
