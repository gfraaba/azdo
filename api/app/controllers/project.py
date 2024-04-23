from flask_restful import Resource
from app.models.project import Project as ProjectModel

class Projects(Resource):
    def get(self):
        return ProjectModel.get_all()

class Project(Resource):
    def get(self, id):
        project = ProjectModel.get(id)
        if project:
            return project
        else:
            return {'message': 'Project not found'}, 404

    def post(self):
        return ProjectModel.create()

    def put(self, id):
        return ProjectModel.update(id)

    def delete(self, id):
        return ProjectModel.delete(id)