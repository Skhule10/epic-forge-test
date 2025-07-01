
from fastapi import FastAPI, Depends, HTTPException
import os
from sap_ai_core import SAPAICoreClient  # hypothetical import for SAP AI Core client

app = FastAPI()

# Environment variables for SAP AI Core configuration
SAP_AI_CORE_URL = os.getenv("SAP_AI_CORE_URL")
SAP_AI_CORE_API_KEY = os.getenv("SAP_AI_CORE_API_KEY")

# Initialize SAP AI Core client
ai_client = SAPAICoreClient(base_url=SAP_AI_CORE_URL, api_key=SAP_AI_CORE_API_KEY)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI SAP AI Core Integration"}

@app.post("/predict/")
async def predict(data: dict):
    try:
        # Send data to SAP AI Core model for prediction
        prediction = ai_client.predict(data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
