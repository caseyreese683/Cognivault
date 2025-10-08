from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.vector_store import VectorStore
from app.services.embeddings import get_embedding

router = APIRouter()
store = VectorStore()

class QueryInput(BaseModel):
    question: str

@router.post("/")
async def query_vault(data: QueryInput):
    query_emb = get_embedding(data.question)
    results = store.query(query_emb)
    return {"results": results}
