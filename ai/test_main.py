import unittest
from fastapi.testclient import TestClient
from .main import app

class TestMainAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_process_query(self):
        response = self.client.post("/query", ={"query": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.())

if __name__ == '__main__':
    unittest.main()
