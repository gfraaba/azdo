from flask_restful import Resource
from app.models.project import Project

class Projects(Resource):
    def get(self):
        return Project.get_all()

    def post(self):
        return Project.create()

    def put(self, id):
        return Project.update(id)

    def delete(self, id):
        return Project.delete(id)