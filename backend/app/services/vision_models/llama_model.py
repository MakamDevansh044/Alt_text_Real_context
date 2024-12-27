from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
from app.core.model_config import ModelConfig

class LlamaVisionModel:
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained(ModelConfig.LLAMA_VISION_MODEL)
        self.model = AutoModelForVision2Seq.from_pretrained(ModelConfig.LLAMA_VISION_MODEL)

    def generate_alt_text(self, image: Image.Image) -> str:
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=100)
        return self.processor.batch_decode(outputs, skip_special_tokens=True)[0] 