import os
from fastapi import FastAPI, Depends, HTTPException
import requests
from typing import List
from pydantic import BaseModel
from .security import get_current_user

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/query")
def process_query(query: Query, user: str = Depends(get_current_user)):
    try:
        external_service_url = os.getenv("EXTERNAL_SERVICE_URL", "https://default-service-url.com")
        response = requests.post(external_service_url, ={"query": query.query}, headers={"Authorization": f"Bearer {user.token}"})
        response.raise_for_status()
        return {"response": response.()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
