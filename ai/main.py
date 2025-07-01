from fastapi import FastAPI, Depends
import requests
from typing import List
from pydantic import BaseModel
from .security import get_current_user

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/query")
def process_query(query: Query, user: str = Depends(get_current_user)):
    response = requests.post("https://sap-ai-core-service-url", ={"query": query.query}, headers={"Authorization": f"Bearer {user.token}"})
    return {"response": response.()}
