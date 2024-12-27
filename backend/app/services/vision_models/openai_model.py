from PIL import Image
import io
import base64
from openai import OpenAI
from app.core.config import Config
from app.core.model_config import ModelConfig
from app.core.exceptions import VisionError

class OpenAIVisionModel:
    def __init__(self):
        if not Config.OPENAI_API_KEY:
            raise VisionError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = ModelConfig.OPENAI_MODEL

    def generate_alt_text(self, image: Image.Image) -> str:
        try:
            # Convert PIL Image to base64
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Generate a detailed description of this image."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=300,
                temperature=0.7,
                presence_penalty=0,
                frequency_penalty=0
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API Error: {str(e)}")  # Debug logging
            raise VisionError(f"OpenAI API Error: {str(e)}") 