from pinecone import Pinecone
from openai import OpenAI
from backend.config import settings
from typing import List, Dict
import logging
import uuid

logger = logging.getLogger(__name__)

class RetrieverService:
    def __init__(self):
        try:
            self.pc = Pinecone(api_key=settings.pinecone_api_key)
            self.index = self.pc.Index(settings.pinecone_index_name)
            self.openai_client = OpenAI(api_key=settings.openai_api_key)
            logger.info(f"Initialized retriever with index: {settings.pinecone_index_name}")
        except Exception as e:
            logger.error(f"Error initializing retriever: {str(e)}")
            raise
    
    def get_embedding(self, text: str) -> List[float]:
        try:
            response = self.openai_client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Error getting embedding: {str(e)}")
            raise
    
    def retrieve_documents(self, query: str, top_k: int = 5) -> List[Dict]:
        try:
            query_embedding = self.get_embedding(query)
            results = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=True
            )
            
            documents = []
            for match in results.matches:
                documents.append({
                    "content": match.metadata.get("content", ""),
                    "source": match.metadata.get("source", "Unknown"),
                    "score": float(match.score),
                    "chunk_index": match.metadata.get("chunk_index", 0)
                })
            
            logger.info(f"Retrieved {len(documents)} documents for query: {query}")
            return documents
        except Exception as e:
            logger.error(f"Error retrieving documents: {str(e)}")
            raise
    
    def store_document(self, chunks: List[str], file_name: str) -> int:
        try:
            vectors_to_upsert = []
            
            for i, chunk in enumerate(chunks):
                embedding = self.get_embedding(chunk)
                chunk_id = f"{file_name}_{i}_{uuid.uuid4().hex[:8]}"
                
                vectors_to_upsert.append((
                    chunk_id,
                    embedding,
                    {
                        "content": chunk,
                        "source": file_name,
                        "chunk_index": i
                    }
                ))
            
            batch_size = 100
            for i in range(0, len(vectors_to_upsert), batch_size):
                batch = vectors_to_upsert[i:i + batch_size]
                self.index.upsert(vectors=batch)
            
            logger.info(f"Stored {len(vectors_to_upsert)} vectors for {file_name}")
            return len(vectors_to_upsert)
        except Exception as e:
            logger.error(f"Error storing document: {str(e)}")
            raise