import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def format_response(context: str, enhanced: str) -> dict:
    return {
        "context": context.strip(),
        "enhanced": enhanced.strip(),
        "word_count": len(context.split())
    }

def log_request(alt_text: str) -> None:
    logger.info(f"Processing alt text: {alt_text[:50]}...")