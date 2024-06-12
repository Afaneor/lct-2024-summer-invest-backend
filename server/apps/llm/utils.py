from server.apps.llm.providers.abstract import AbstractLLMProvider


def get_llm_provider() -> AbstractLLMProvider:
    from django.conf import settings
    from django.utils.module_loading import import_string
    klass = import_string(settings.LLM_PROVIDER)
    if not issubclass(klass, AbstractLLMProvider):
        raise ValueError('LLM provider must be a subclass of Abstract LLm Provider')
    return klass()
