
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
    # Integration with SAP AI Core
    try:
        # Assuming SAP AI Core endpoint and credentials are set as environment variables
        ai_core_endpoint = os.getenv("AI_CORE_ENDPOINT")
        ai_core_api_key = os.getenv("AI_CORE_API_KEY")
        
        response = requests.post(ai_core_endpoint, ={"text": message.text}, headers={"Authorization": f"Bearer {ai_core_api_key}"})
        response.raise_for_status()
        return response.()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    return {"Hello": "World"}
