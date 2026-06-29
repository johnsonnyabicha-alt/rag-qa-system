from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DocumentUploadRequest(BaseModel):
    file_name: str
    content: str

class SourceDocument(BaseModel):
    content: str
    source: str
    score: float
    chunk_index: Optional[int] = None

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]
    confidence: float
    query: str