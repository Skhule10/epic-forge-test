import unittest
from fastapi.testclient import TestClient
from copilot.ai.main import app

class TestFastAPIIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.(), {"message": "Welcome to the FastAPI SAP AI Core Integration"})

    def test_predict(self):
        data = {"input": "test data"}
        response = self.client.post("/predict/", =data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.())

    def test_error_handling(self):
        # Test for error handling
        response = self.client.post("/process-query", ={})
        self.assertEqual(response.status_code, 400)  # Assuming 400 for bad request

if __name__ == "__main__":
    unittest.main()
