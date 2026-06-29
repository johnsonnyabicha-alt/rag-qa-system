from fastapi import APIRouter, HTTPException
from backend.models.schemas import QueryRequest, QueryResponse, SourceDocument
from backend.services.retriever import RetrieverService
from backend.services.llm import LLMService
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["query"])

retriever = RetrieverService()
llm = LLMService()

@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    try:
        logger.info(f"Processing query: {request.query}")
        documents = retriever.retrieve_documents(request.query, top_k=request.top_k)
        
        if not documents:
            return QueryResponse(
                answer="No relevant documents found in the knowledge base. Please upload documents first.",
                sources=[],
                confidence=0.0,
                query=request.query
            )
        
        context = llm.format_context(documents)
        answer = llm.generate_answer(request.query, context)
        source_scores = [doc["score"] for doc in documents]
        confidence = llm.calculate_confidence(source_scores)
        
        sources = [
            SourceDocument(
                content=doc["content"],
                source=doc["source"],
                score=doc["score"],
                chunk_index=doc.get("chunk_index", 0)
            )
            for doc in documents
        ]
        
        logger.info(f"Successfully answered query with {len(sources)} sources")
        return QueryResponse(
            answer=answer,
            sources=sources,
            confidence=confidence,
            query=request.query
        )
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")