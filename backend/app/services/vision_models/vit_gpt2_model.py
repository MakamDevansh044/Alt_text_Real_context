from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

from app.core.model_config import ModelConfig

class VitGPT2Model:
    def __init__(self):
        self.model = VisionEncoderDecoderModel.from_pretrained(ModelConfig.VIT_GPT2_MODEL)
        self.feature_extractor = ViTImageProcessor.from_pretrained(ModelConfig.VIT_GPT2_MODEL)
        self.tokenizer = AutoTokenizer.from_pretrained(ModelConfig.VIT_GPT2_MODEL)

    def generate_alt_text(self, image: Image.Image) -> str:
        # Resize image to expected size
        image = image.resize((224, 224))
        
        # Process image
        pixel_values = self.feature_extractor(images=image, return_tensors="pt").pixel_values
        
        with torch.no_grad():
            outputs = self.model.generate(
                pixel_values,
                max_length=30,
                num_beams=4,
                temperature=0.7
            )
            
        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0] 