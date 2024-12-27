import openai
from app.core.config import Config
from app.core.exceptions import OpenAIError

class OpenAIService:
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY

    def enhance_context(self, context: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "system",
                    "content": "You are a context enhancement specialist."
                }, {
                    "role": "user",
                    "content": f"Enhance this context: {context}"
                }]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise OpenAIError(f"Error enhancing context: {str(e)}")