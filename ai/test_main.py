import unittest
from fastapi.testclient import TestClient
from main import app

class TestFastAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_process_data(self):
        response = self.client.post("/process/", ={"text": "hello"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.(), {"processed_text": "HELLO"})

    def test_missing_token(self):
        response = self.client.post("/process/", ={"text": "hello"})
        self.assertEqual(response.status_code, 401)
        self.assertIn("Missing authorization token", response.()["detail"])

if __name__ == "__main__":
    unittest.main()
