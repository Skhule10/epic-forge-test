
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

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
            query_response = response.().get("response")
            # Log the query response
            logging.info(f"Query Response: {query_response}")
            return {"response": query_response}
        else:
            raise HTTPException(status_code=response.status_code, detail="Error processing query")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    