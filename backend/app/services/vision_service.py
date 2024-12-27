from PIL import Image
import io
from app.core.model_config import ModelType
from app.core.exceptions import VisionError
from app.services.vision_models.huggingface_model import HuggingFaceVisionModel

class VisionService:
    def __init__(self, model_type: ModelType = ModelType.HUGGINGFACE):
        self.model_type = model_type
        self.model = self._load_model()

    def _load_model(self):
        try:
            if self.model_type == ModelType.HUGGINGFACE:
                return HuggingFaceVisionModel()
            else:
                raise VisionError(f"Unsupported model type: {self.model_type}")
        except Exception as e:
            raise VisionError(f"Failed to load model: {str(e)}")

    def generate_alt_text(self, image_bytes: bytes) -> str:
        try:
            # Convert bytes to PIL Image
            image = Image.open(io.BytesIO(image_bytes))
            return self.model.generate_alt_text(image)
        except Exception as e:
            raise VisionError(f"Error generating alt text: {str(e)}")

    def switch_model(self, model_type: str):
        try:
            self.model_type = ModelType(model_type)
            self.model = self._load_model()
        except Exception as e:
            raise VisionError(f"Failed to switch model: {str(e)}")