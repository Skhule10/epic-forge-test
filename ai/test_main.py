import pytest
from fastapi.testclient import TestClient
from .main import app
from .security import verify_xsuaa_token

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

def test_process_message():
    response = client.post("/process", ={"message": "Test message"})
    assert response.status_code == 200
    assert response.() == {"processed_message": "Processed Test message with SAP AI Core"}

def test_verify_xsuaa_token():
    request_mock = Request(headers={"Authorization": "Bearer test_token"})
    try:
        decoded_token = verify_xsuaa_token(request_mock)
        assert decoded_token is not None
    except HTTPException as e:
        assert e.status_code == 401