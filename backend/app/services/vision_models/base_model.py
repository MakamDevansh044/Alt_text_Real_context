from abc import ABC, abstractmethod
from PIL import Image

class BaseVisionModel(ABC):
    @abstractmethod
    def generate_alt_text(self, image: Image.Image) -> str:
        pass 