from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/process")
async def process_message(message: str):
    # Integrate with SAP AI Core LLM model here
    return {"processed_message": message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
