from domain import project_domain
from backend import app, mongo_client
from flask_pymongo import PyMongo


def create_project():
    project_id = project_domain.ProjectDomain.generate_id()
    project = project_domain.ProjectDomain.create_default_project(project_id, 'owner_id')

    mongo_client.db.projects.insert_one(project.__dict__)
    print('Project Created with id ', project_id)


def get_projects(project_count = 5, current_project_itr = 0):
    pass
