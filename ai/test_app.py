import os
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

def test_send_message_success():
    """Test sending a message successfully."""
    os.environ["AI_CORE_ENDPOINT"] = "http://mock-ai-core-endpoint"
    os.environ["AI_CORE_API_KEY"] = "mock-api-key"

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 200
    assert "text" in response.()

def test_send_message_missing_endpoint():
    """Test sending a message with missing endpoint."""
    os.environ.pop("AI_CORE_ENDPOINT", None)
    os.environ["AI_CORE_API_KEY"] = "mock-api-key"

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 500
    assert response.()["detail"] == "AI Core configuration is missing"

def test_send_message_invalid_api_key():
    """Test sending a message with invalid API key."""
    os.environ["AI_CORE_ENDPOINT"] = "http://mock-ai-core-endpoint"
    os.environ["AI_CORE_API_KEY"] = "invalid-api-key"

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 500
    assert "Request error occurred" in response.()["detail"]
