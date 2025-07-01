import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import requests

# Initialize FastAPI
app = FastAPI()

# Security setup using OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# SAP AI Core configuration
SAP_AI_CORE_URL = os.getenv("SAP_AI_CORE_URL")
SAP_AI_CORE_API_KEY = os.getenv("SAP_AI_CORE_API_KEY")

# Secure routing with app router
@app.get("/secure-data")
async def get_secure_data(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {SAP_AI_CORE_API_KEY}"}
    try:
        response = requests.get(f"{SAP_AI_CORE_URL}/data", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP error responses
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response.()

# Endpoint for SAP AI Core LLM interaction
@app.post("/process-query")
async def process_query(query: str):
    headers = {"Authorization": f"Bearer {SAP_AI_CORE_API_KEY}"}
    data = {"query": query}
    try:
        response = requests.post(f"{SAP_AI_CORE_URL}/llm", headers=headers, =data)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response.()
