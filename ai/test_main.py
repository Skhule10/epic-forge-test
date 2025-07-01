
import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_secure_data():
    response = client.get("/secure-data")
    assert response.status_code == 200
    assert "data" in response.()

def test_process_query():
    response = client.post("/process-query", ={"query": "Hello, SAP AI!"})
    assert response.status_code == 200
    assert "response" in response.()
