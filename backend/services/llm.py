from openai import OpenAI
from backend.config import settings
import logging

logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
    
    def generate_answer(self, query: str, context: str) -> str:
        try:
            system_prompt = """You are an expert in philosophy, politics, and economics. Your role is to provide accurate, well-reasoned answers based on the provided context. If the context doesn't contain relevant information, say 'I don't have enough information in the provided documents to answer this question.' Always be objective and balanced, especially on political topics."""
            
            user_prompt = f"""Based on the following context, answer the question:

CONTEXT:
{context}

QUESTION: {query}

Provide a comprehensive answer using only the information from the context above."""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            answer = response.choices[0].message.content
            logger.info(f"Generated answer for query: {query[:50]}...")
            return answer
        except Exception as e:
            logger.error(f"Error generating answer: {str(e)}")
            raise
    
    def calculate_confidence(self, sources_scores: list) -> float:
        if not sources_scores:
            return 0.0
        avg_score = sum(sources_scores) / len(sources_scores)
        return min(avg_score, 1.0)
    
    def format_context(self, documents: list) -> str:
        context_parts = []
        for i, doc in enumerate(documents, 1):
            formatted_doc = f"[Source {i}: {doc['source']}]\n{doc['content']}"
            context_parts.append(formatted_doc)
        return "\n\n".join(context_parts)