
import os
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

def test_predict():
    # Simulate OAuth2 token
    token = "test_token"
    response = client.get("/predict/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.() == {"prediction": "result"}
