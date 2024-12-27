from typing import Union
from app.core.model_config import ModelType
from app.core.exceptions import ModelLoadError
from app.services.vision_models.openai_model import OpenAIVisionModel
from app.services.vision_models.gemini_model import GeminiVisionModel
from app.services.vision_models.huggingface_model import HuggingFaceVisionModel

class VisionModelFactory:
    @staticmethod
    def get_model(model_type: Union[str, ModelType]):
        try:
            if isinstance(model_type, str):
                model_type = ModelType(model_type)

            if model_type == ModelType.OPENAI:
                return OpenAIVisionModel()
            elif model_type == ModelType.GEMINI:
                return GeminiVisionModel()
            elif model_type == ModelType.HUGGINGFACE:
                return HuggingFaceVisionModel()
            else:
                raise ValueError(f"Unsupported model type: {model_type}")
        except Exception as e:
            raise ModelLoadError(f"Failed to load model {model_type}: {str(e)}") 