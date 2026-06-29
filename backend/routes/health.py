from fastapi import APIRouter, HTTPException
from backend.services.retriever import RetrieverService
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "PPE RAG Q&A System", "version": "1.0.0"}

@router.get("/api/health")
async def api_health_check():
    try:
        retriever = RetrieverService()
        return {"status": "healthy", "api": "operational", "vector_db": "connected", "llm": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")