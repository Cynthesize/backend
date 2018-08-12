from domain import project_domain
from backend import app, mongo_client
from flask_pymongo import PyMongo


def create_project(self):
    project_id = project_domain.ProjectDomain.generate_id()
    project = project_domain.ProjectDomain(project_id, owner_id)

    mongo_client.db.projects.insert_one(project)
    