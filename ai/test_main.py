import unittest
from fastapi.testclient import TestClient
from main import app

class TestFastAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_process_query(self):
        response = self.client.post("/processQuery", ={"query": "Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.())

    def test_error_handling(self):
        response = self.client.post("/processQuery", ={"query": ""})
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("detail", response.())

if __name__ == '__main__':
    unittest.main()
