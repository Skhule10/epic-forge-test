from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/process")
async def process_message(message: str):
    try:
        processed_message = f"Processed {message} with SAP AI Core"
        return {"processed_message": processed_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))