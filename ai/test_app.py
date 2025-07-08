import os
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

@patch('requests.post')
def test_send_message_success(mock_post):
    """Test sending a message successfully."""
    os.environ["AI_CORE_ENDPOINT"] = "http://mock-ai-core-endpoint"
    os.environ["AI_CORE_API_KEY"] = "mock-api-key"

    mock_post.return_value.status_code = 200
    mock_post.return_value..return_value = {"response": "Success"}

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 200
    assert response.() == {"status": "Success", "data": {"response": "Success"}}

def test_send_message_missing_endpoint():
    """Test sending a message with missing endpoint."""
    os.environ.pop("AI_CORE_ENDPOINT", None)
    os.environ["AI_CORE_API_KEY"] = "mock-api-key"

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 500
    assert response.()["detail"] == "AI Core endpoint configuration is missing"

def test_send_message_missing_api_key():
    """Test sending a message with missing API key."""
    os.environ["AI_CORE_ENDPOINT"] = "http://mock-ai-core-endpoint"
    os.environ.pop("AI_CORE_API_KEY", None)

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 500
    assert response.()["detail"] == "AI Core API key configuration is missing"

@patch('requests.post')
def test_send_message_invalid_api_key(mock_post):
    """Test sending a message with invalid API key."""
    os.environ["AI_CORE_ENDPOINT"] = "http://mock-ai-core-endpoint"
    os.environ["AI_CORE_API_KEY"] = "invalid-api-key"

    mock_post.side_effect = Exception("Invalid API key")

    response = client.post("/send/", ={"text": "Hello", "author": "John Doe"})
    assert response.status_code == 500
    assert "Request error occurred" in response.()["detail"]
