import google.generativeai as genai
from PIL import Image
from app.core.config import Config
from app.core.exceptions import VisionError

class GeminiVisionModel:
    def __init__(self):
        if not Config.GEMINI_API_KEY:
            raise VisionError("Gemini API key not found in environment variables")
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro-vision')

    def generate_alt_text(self, image: Image.Image) -> str:
        try:
            response = self.model.generate_content([
                "Generate a detailed description of this image.",
                image
            ], generation_config={
                "max_output_tokens": 1024,
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40
            })
            return response.text
        except Exception as e:
            print(f"Gemini API Error: {str(e)}")  # Debug logging
            raise VisionError(f"Gemini API Error: {str(e)}") 