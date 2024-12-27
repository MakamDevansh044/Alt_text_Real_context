import pytest
from app.services.openai_service import OpenAIService
from app.core.exceptions import OpenAIError

def test_enhance_context():
    service = OpenAIService()
    context = "Basic context about a scene"
    result = service.enhance_context(context)
    assert isinstance(result, str)
    assert len(result) > len(context)

def test_invalid_input():
    service = OpenAIService()
    with pytest.raises(OpenAIError):
        service.enhance_context("")