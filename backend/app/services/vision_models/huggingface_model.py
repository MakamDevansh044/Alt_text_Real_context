import requests
from PIL import Image
import io
from app.core.config import Config
from app.core.exceptions import VisionError

class HuggingFaceVisionModel:
    def __init__(self):
        if not Config.HUGGINGFACE_API_KEY:
            raise VisionError("Hugging Face API key not found in environment variables")
        self.api_key = Config.HUGGINGFACE_API_KEY
        self.api_url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def test_connection(self):
        """Test the API connection and token validity"""
        try:
            response = requests.get(self.api_url, headers=self.headers)
            if response.status_code == 200:
                return True
            print(f"Connection test failed: {response.text}")
            return False
        except Exception as e:
            print(f"Connection test error: {str(e)}")
            return False

    def generate_alt_text(self, image: Image.Image) -> str:
        try:
            # Test connection first
            if not self.test_connection():
                raise VisionError("Failed to connect to Hugging Face API. Please check your API token.")

            # Convert PIL Image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            response = requests.post(
                self.api_url,
                headers=self.headers,
                data=img_byte_arr,
                timeout=30  # Add timeout
            )
            
            print(f"HF Response Status: {response.status_code}")  # Debug logging
            print(f"HF Response Headers: {response.headers}")  # Debug logging
            
            if response.status_code != 200:
                print(f"HF Error Response: {response.text}")  # Debug logging
                raise VisionError(f"API request failed: {response.text}")

            result = response.json()
            print(f"HF Response Body: {result}")  # Debug logging
            
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', '')
            
            raise VisionError("Unexpected response format")
            
        except requests.exceptions.RequestException as e:
            print(f"Network error: {str(e)}")
            raise VisionError(f"Network error: {str(e)}")
        except Exception as e:
            print(f"Hugging Face API Error: {str(e)}")
            raise VisionError(f"Hugging Face API Error: {str(e)}") 