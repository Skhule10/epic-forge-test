from fastapi import FastAPI, Depends, HTTPException
import os
import logging
from sap_ai_core import SAPAICoreClient  # hypothetical import for SAP AI Core client

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables for SAP AI Core configuration
SAP_AI_CORE_URL = os.getenv("SAP_AI_CORE_URL")
SAP_AI_CORE_API_KEY = os.getenv("SAP_AI_CORE_API_KEY")

# Initialize SAP AI Core client
try:
    ai_client = SAPAICoreClient(base_url=SAP_AI_CORE_URL, api_key=SAP_AI_CORE_API_KEY)
    logger.info("SAP AI Core client initialized successfully.")
except Exception as e:
    logger.error(f"Error initializing SAP AI Core client: {e}")
    raise HTTPException(status_code=500, detail="Failed to initialize AI client")

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the FastAPI SAP AI Core Integration"}

@app.post("/predict/")
async def predict(data: dict):
    try:
        # Send data to SAP AI Core model for prediction
        logger.info("Predict endpoint accessed")
        prediction = ai_client.predict(data)
        logger.info(f"Prediction successful: {prediction}")
        return {"prediction": prediction}
    except ValueError as ve:
        logger.error(f"Value error during prediction: {ve}")
        raise HTTPException(status_code=400, detail="Invalid input data")
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed due to server error")