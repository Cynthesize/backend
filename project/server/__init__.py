# project/server/__init__.py

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from project.server.controllers.login_views import auth_blueprint


app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)

app.register_blueprint(auth_blueprint)
