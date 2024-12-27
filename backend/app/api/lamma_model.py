import logging
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
from PIL import Image

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_alt_text(image_path):
    try:
        # Load model and processor
        logger.info("Loading BLIP-2 model and processor...")
        model_name = "Salesforce/blip2-opt-2.7b"
        processor = AutoProcessor.from_pretrained(model_name)
        model = AutoModelForImageTextToText.from_pretrained(model_name)
        
        # Load image
        logger.info(f"Loading image from {image_path}")
        image = Image.open(image_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        # Process image
        logger.info("Processing image...")
        inputs = processor(images=image, return_tensors="pt")
        
        # Generate text
        logger.info("Generating alt text...")
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=100,
                num_beams=5,
                temperature=0.7
            )
        
        # Decode output
        alt_text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
        logger.info("Alt text generation complete!")
        
        return alt_text
        
    except Exception as e:
        logger.error(f"Error generating alt text: {str(e)}")
        raise

if __name__ == "__main__":
    # Replace with your image path
    image_path = "app/api/image.jpg"
    
    try:
        alt_text = generate_alt_text(image_path)
        print("\nGenerated Alt Text:")
        print("-" * 50)
        print(alt_text)
        print("-" * 50)
    except Exception as e:
        logger.error(f"Failed to process image: {str(e)}")