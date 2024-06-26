import sys, os, unittest, json

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, mock_data
from app.models.project import Project

# cd /workspaces/azdo/api/tests
# python -m unittest test_projects.py
class TestProjectsAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # Seed the database
        Project.seed(mock_data)

    def test_get_projects_count(self):
        response = self.client.get('/api/projects')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 10)

    def test_get_first_project(self):
        response = self.client.get('/api/project/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['projectName'], 'Apollo')

if __name__ == '__main__':
    unittest.main()