import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    DEBUG = os.getenv('DEBUG', False)

    @classmethod
    def validate(cls):
        if not cls.HUGGINGFACE_API_KEY:
            raise ValueError("HUGGINGFACE_API_KEY not found in environment variables")

# Validate configuration on import
Config.validate()