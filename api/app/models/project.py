from tinydb import TinyDB, Query
from flask import request

db = TinyDB('db.json')
ProjectQuery = Query()

class Project:
    @staticmethod
    def get_all():
        return db.table('projects').all()

    @staticmethod
    def create():
        new_project = request.get_json()
        db.table('projects').insert(new_project)
        return new_project, 201

    @staticmethod
    def update(id):
        updated_project = request.get_json()
        db.table('projects').update(updated_project, ProjectQuery.id == id)
        return updated_project, 200

    @staticmethod
    def delete(id):
        db.table('projects').remove(ProjectQuery.id == id)
        return '', 204
    
    @staticmethod
    def seed(mock_data):
        db.table('projects').truncate()
        for project_data in mock_data:
            db.table('projects').upsert(project_data, ProjectQuery.projectName == project_data['projectName'])