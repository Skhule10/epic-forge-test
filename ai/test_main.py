import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

def test_process_message():
    response = client.post("/process", ={"message": "Test message"})
    assert response.status_code == 200
    assert response.() == {"processed_message": "Test message"}