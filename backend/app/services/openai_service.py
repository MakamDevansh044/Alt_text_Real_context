# app/services/openai_service.py
from openai import OpenAI
from app.core.config import Config
from app.core.exceptions import OpenAIError

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def enhance_context(self, context: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a context enhancement specialist."},
                    {"role": "user", "content": f"Enhance this context: {context}"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise OpenAIError(f"Error enhancing context: {str(e)}")