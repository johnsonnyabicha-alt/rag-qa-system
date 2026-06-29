from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # OpenAI Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = "gpt-3.5-turbo"
    
    # Pinecone Configuration
    pinecone_api_key: str = os.getenv("PINECONE_API_KEY", "")
    pinecone_index_name: str = os.getenv("PINECONE_INDEX_NAME", "ppe-reg-qa-system")
    pinecone_environment: str = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")
    
    # Database Configuration
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./ppe_qa.db")
    
    # Server Configuration
    debug: bool = os.getenv("DEBUG", "True") == "True"
    port: int = int(os.getenv("PORT", "8000"))
    host: str = os.getenv("HOST", "0.0.0.0")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()