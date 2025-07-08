
import os
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

def test_send_message():
    os.environ["AI_CORE_ENDPOINT"] = "http://mock-ai-core-endpoint"
    os.environ["AI_CORE_API_KEY"] = "mock-api-key"

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 200
    assert "text" in response.()
