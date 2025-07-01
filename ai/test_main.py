
import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
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

    @patch('main.requests.post')
    def test_invalid_token(self, mock_post):
        mock_post.return_value.status_code = 401
        response = self.client.post("/processQuery", ={"query": "Hello"})
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.())

    @patch('main.requests.post')
    def test_invalid_url(self, mock_post):
        mock_post.side_effect = Exception("Invalid URL")
        response = self.client.post("/processQuery", ={"query": "Hello"})
        self.assertEqual(response.status_code, 500)
        self.assertIn("detail", response.())

    def test_edge_case_long_query(self):
        long_query = "x" * 10000
        response = self.client.post("/processQuery", ={"query": long_query})
        self.assertIn("response", response.())

    def test_edge_case_special_characters(self):
        special_query = "!@#$%^&*()"
        response = self.client.post("/processQuery", ={"query": special_query})
        self.assertIn("response", response.())

if __name__ == '__main__':
    unittest.main()
