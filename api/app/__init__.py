from flask import Flask
from flask import jsonify
# from flask_restful import Api
# from .controllers import projects, repos, branches, commits

app = Flask(__name__)
# api = Api(app)

# api.add_resource(projects.Projects, '/api/projects')
# api.add_resource(repos.Repos, '/api/repos')
# api.add_resource(branches.Branches, '/api/branches')
# api.add_resource(commits.Commits, '/api/commits')

mock_data = [
    {
        'projectName': 'Project 1',
        'repos': [
            {
                'repoName': 'Repo 1',
                'branches': [
                    {
                        'branchName': 'Branch 1',
                        'commits': ['Commit 1', 'Commit 2']
                    },
                    {
                        'branchName': 'Branch 2',
                        'commits': ['Commit 3', 'Commit 4']
                    }
                ]
            },
            {
                'repoName': 'Repo 2',
                'branches': [
                    {
                        'branchName': 'Branch 3',
                        'commits': ['Commit 5', 'Commit 6']
                    }
                ]
            }
        ]
    },
    # Add more projects here...
]

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify(mock_data)