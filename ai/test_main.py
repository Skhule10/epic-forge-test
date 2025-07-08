
import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_ai_data():
    response = client.get("/ai")
    assert response.status_code == 200
    assert "resources" in response.()

def test_secure_endpoint():
    os.environ["XSUAA_CLIENT_ID"] = "test_client_id"
    os.environ["XSUAA_CLIENT_SECRET"] = "test_client_secret"
    os.environ["XSUAA_AUTH_ENDPOINT"] = "https://test-auth.endpoint"
    
    response = client.get("/secure")
    assert response.status_code == 200
    assert response.() == {"message": "Secure endpoint accessed"}
