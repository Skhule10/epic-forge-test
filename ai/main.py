from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/processQuery")
async def process_query(request: QueryRequest):
    try:
        # Integration with SAP AI Core
        url = os.getenv("SAP_AI_CORE_URL")  # Use environment variable for SAP AI Core URL
        headers = {"Authorization": f"Bearer {os.getenv('SAP_AI_CORE_TOKEN')}"}
        response = requests.post(url, ={"query": request.query}, headers=headers)

        if response.status_code == 200:
            return {"response": response.().get("response")}
        else:
            raise HTTPException(status_code=response.status_code, detail="Error processing query")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
