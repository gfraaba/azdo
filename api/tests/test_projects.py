import sys
import os
import unittest
import json

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestProjectsAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_projects(self):
        response = self.client.get('/api/projects')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[0]['projectName'], 'Project 1')

if __name__ == '__main__':
    unittest.main()