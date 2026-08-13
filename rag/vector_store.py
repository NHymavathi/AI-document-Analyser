from typing import List, Dict, Any
import math
import re

class SimpleVectorStore:
    """In-memory lightweight Vector RAG store with TF-IDF / Cosine Similarity matching."""
    def __init__(self):
        self.documents: List[Dict[str, Any]] = []

    def add_documents(self, docs: List[Dict[str, Any]]):
        """Docs schema: [{'content': text, 'source': file_name, 'location': page_or_row}]"""
        self.documents.extend(docs)

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r'\w+', text.lower())

    def search(self, query: str, k: int = 3) -> List[Dict[str, Any]]:
        query_tokens = set(self._tokenize(query))
        if not query_tokens or not self.documents:
            return self.documents[:k]
        
        scored_docs = []
        for doc in self.documents:
            doc_tokens = self._tokenize(doc['content'])
            doc_token_set = set(doc_tokens)
            overlap = query_tokens.intersection(doc_token_set)
            score = len(overlap) / (math.sqrt(len(query_tokens)) * math.sqrt(max(len(doc_token_set), 1)))
            scored_docs.append((score, doc))

        scored_docs.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored_docs[:k]]

# Global RAG Instance per application lifetime
vector_rag_store = SimpleVectorStore()
