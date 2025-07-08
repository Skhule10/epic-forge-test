import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

class Message(BaseModel):
    text: str
    author: str

app = FastAPI()

@app.post("/send/")
async def send_message(message: Message):
    """
    Endpoint to send a message to SAP AI Core.
    The integration uses environment variables for configuration.
    """
    try:
        # Retrieve SAP AI Core endpoint and credentials from environment variables
        ai_core_endpoint = os.getenv("AI_CORE_ENDPOINT")
        ai_core_api_key = os.getenv("AI_CORE_API_KEY")

        if not ai_core_endpoint:
            raise HTTPException(status_code=500, detail="AI Core endpoint configuration is missing")
        if not ai_core_api_key:
            raise HTTPException(status_code=500, detail="AI Core API key configuration is missing")

        # Send a POST request to the SAP AI Core endpoint
        response = requests.post(
            ai_core_endpoint,
            ={"text": message.text},
            headers={"Authorization": f"Bearer {ai_core_api_key}"}
        )
        
        # Check for request exceptions
        response.raise_for_status()

        # Process and return the response from SAP AI Core
        response_data = response.()
        return {"status": "Success", "data": response_data}
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise HTTPException(status_code=500, detail=f"Request error occurred: {req_err}")

@app.get("/")
async def read_root():
    """
    Root endpoint providing a simple greeting.
    """
    return {"Hello": "World"}
