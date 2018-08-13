from backend import app
from domain import project_services

@app.route("/")
def index():
    return "Hello World"

@app.route("/add-project", methods = ['GET'])
def add_project():
    project_services.create_project()
    return "Project created!!"
