import pytest
from app.services.langchain_service import LangChainService
from app.core.exceptions import LangChainError

def test_generate_context():
    service = LangChainService()
    alt_text = "A dog playing in the park"
    result = service.generate_context(alt_text)
    assert isinstance(result, str)
    assert len(result) > 0

def test_invalid_input():
    service = LangChainService()
    with pytest.raises(LangChainError):
        service.generate_context("")