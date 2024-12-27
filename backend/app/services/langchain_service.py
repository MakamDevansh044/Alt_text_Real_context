from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from app.core.config import Config
from app.core.exceptions import LangChainError

class LangChainService:
    def __init__(self):
        try:
            self.llm = ChatOpenAI(
                api_key=Config.OPENAI_API_KEY,
                model_name="gpt-4",
                temperature=0.7
            )
            
            self.prompt = PromptTemplate(
                input_variables=["alt_text"],
                template="Given this image description: {alt_text}\n\nProvide additional context and details about what this image might represent or symbolize."
            )
            
            self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
        except Exception as e:
            raise LangChainError(f"Failed to initialize LangChain service: {str(e)}")

    def generate_context(self, alt_text: str) -> str:
        try:
            response = self.chain.run(alt_text=alt_text)
            return response.strip()
        except Exception as e:
            raise LangChainError(f"Error generating context: {str(e)}")