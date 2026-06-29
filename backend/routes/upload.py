from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.services.document_processor import DocumentProcessor
from backend.services.retriever import RetrieverService
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["documents"])

processor = DocumentProcessor()
retriever = RetrieverService()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        logger.info(f"Processing upload for file: {file.filename}")
        content = await file.read()
        
        try:
            content_str = content.decode('utf-8')
        except UnicodeDecodeError:
            content_str = content.decode('latin-1')
        
        if not content_str.strip():
            raise ValueError("File is empty")
        
        chunks = processor.process_document(content_str, file.filename)
        
        if not chunks:
            raise ValueError("No content could be extracted from file")
        
        vector_count = retriever.store_document(chunks, file.filename)
        logger.info(f"Successfully uploaded {file.filename}: {len(chunks)} chunks, {vector_count} vectors")
        
        return {
            "message": f"Document '{file.filename}' uploaded successfully",
            "chunks": len(chunks),
            "filename": file.filename,
            "chunk_count": vector_count
        }
    except Exception as e:
        logger.error(f"Error uploading document {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error uploading document: {str(e)}")