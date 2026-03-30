# FastAPI entry point

from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.pipeline import rag_pipeline

app = FastAPI()

class QueryRequest(BaseModel):
    query : str

@app.post("/query")
def query_rag(req : QueryRequest):
    return rag_pipeline(req.query)