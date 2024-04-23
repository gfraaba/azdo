from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from .controllers import project
from .models.project import Project
from .data_seeder import get_mock_data

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(project.Projects, '/api/projects')
api.add_resource(project.Project, '/api/project/<string:id>')

mock_data = get_mock_data()

# Seed the database
Project.seed(mock_data)

# @app.route('/api/projects', methods=['GET'])
# def get_projects():
#     return jsonify(mock_data)