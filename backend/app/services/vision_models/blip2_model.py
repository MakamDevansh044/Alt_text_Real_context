from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
from PIL import Image
from app.core.model_config import ModelConfig

class BLIP2Model:
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained(ModelConfig.BLIP2_MODEL)
        self.model = AutoModelForImageTextToText.from_pretrained(ModelConfig.BLIP2_MODEL)

    def generate_alt_text(self, image: Image.Image) -> str:
        inputs = self.processor(images=image, return_tensors="pt")
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=100,
                num_beams=5,
                temperature=0.7
            )
        
        return self.processor.batch_decode(outputs, skip_special_tokens=True)[0] 