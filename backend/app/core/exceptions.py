class BaseError(Exception):
    """Base exception class for the application."""
    pass

class VisionError(BaseError):
    """Exception raised for errors in the vision service."""
    pass

class OpenAIError(BaseError):
    """Exception raised for errors in OpenAI service."""
    pass

class ModelLoadError(BaseError):
    """Exception raised when loading a model fails."""
    pass

class LangChainError(BaseError):
    """Exception raised for errors in LangChain service."""
    pass

class ProcessingError(BaseError):
    """Exception raised for general processing errors."""
    pass