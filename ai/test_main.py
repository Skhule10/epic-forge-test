import unittest
from fastapi.testclient import TestClient
from .main import app

class TestMainAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_process_query_success(self):
        response = self.client.post("/query", ={"query": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.())

    def test_process_query_missing_query(self):
        response = self.client.post("/query", ={})
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_process_query_invalid_token(self):
        # Simulate invalid token scenario
        response = self.client.post("/query", ={"query": "Test"}, headers={"Authorization": "Bearer invalid_token"})
        self.assertEqual(response.status_code, 401)  # Unauthorized

    def test_external_service_error_handling(self):
        # Simulate external service error
        with unittest.mock.patch("requests.post", side_effect=requests.exceptions.ConnectionError):
            response = self.client.post("/query", ={"query": "Test"})
            self.assertEqual(response.status_code, 500)  # Internal Server Error

if __name__ == '__main__':
    unittest.main()
