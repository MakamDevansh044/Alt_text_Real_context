from enum import Enum
from dataclasses import dataclass

class ModelType(Enum):
    HUGGINGFACE = "huggingface"

@dataclass
class ModelConfig:
    HUGGINGFACE_MODEL = "Salesforce/blip-image-captioning-large"
    DEFAULT_MODEL = ModelType.HUGGINGFACE 