from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import logging

logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 50):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def process_document(self, content: str, file_name: str) -> List[str]:
        try:
            chunks = self.splitter.split_text(content)
            logger.info(f"Processed {file_name}: {len(chunks)} chunks created")
            return chunks
        except Exception as e:
            logger.error(f"Error processing document {file_name}: {str(e)}")
            raise