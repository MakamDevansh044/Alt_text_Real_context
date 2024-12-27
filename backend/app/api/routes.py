from flask import Blueprint, request, jsonify
from app.services.vision_service import VisionService
from app.services.sentiment_service import SentimentService
from app.core.model_config import ModelType
from app.core.exceptions import VisionError
import re

bp = Blueprint('api', __name__, url_prefix='/api')

vision_service = VisionService(model_type=ModelType.HUGGINGFACE)
sentiment_service = SentimentService()

def generate_context(alt_text: str) -> str:
    # Generate basic context
    context = f"The image shows {alt_text}. This appears to be a scene featuring {alt_text.lower()}."
    return context

def generate_enhanced_context(alt_text: str, context: str) -> str:
    # Clean and normalize the text
    cleaned_text = alt_text.strip().lower()
    
    # Extract key elements
    subjects = re.findall(r'(?:a |an |the )?([a-z]+(?:\s+[a-z]+)?)', cleaned_text)
    actions = re.findall(r'(?:is |are |was |were )?([a-z]+ing|[a-z]+s\b)', cleaned_text)
    descriptors = re.findall(r'([a-z]+ly|[a-z]+ful|[a-z]+ish|[a-z]+ic)\b', cleaned_text)
    
    # Build enhanced description
    parts = []
    parts.append(context)  # Start with the basic context
    
    # Add detailed analysis
    if subjects:
        parts.append(f"The main elements captured include {', '.join(subjects)}.")
    
    if actions:
        parts.append(f"The scene depicts {', '.join(actions)}.")
    
    if descriptors:
        parts.append(f"The image conveys a {', '.join(descriptors)} atmosphere.")
    
    # Add visual interpretation
    parts.append("From a visual perspective, " + 
                f"this image effectively captures {subjects[-1] if subjects else 'the scene'} " +
                "with its natural composition and setting.")
    
    return ' '.join(parts)

@bp.route('/process-image', methods=['POST'])
def process_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
            
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Process the image
        image_bytes = file.read()
        alt_text = vision_service.generate_alt_text(image_bytes)
        
        # Generate context and enhanced context
        context = generate_context(alt_text)
        enhanced_context = generate_enhanced_context(alt_text, context)
        
        # Analyze sentiment
        sentiment = sentiment_service.analyze_sentiment(enhanced_context)
        
        response_data = {
            "alt_text": alt_text,
            "context": context,
            "enhanced_context": enhanced_context,
            "sentiment_analysis": sentiment
        }
        
        return jsonify(response_data)
        
    except VisionError as e:
        return jsonify({"error": str(e)}), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "API is working"})