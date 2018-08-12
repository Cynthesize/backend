
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
mongo_uri = 'mongodb://127.0.0.1:27017/wareahaus'

from backend.routes import *

mongo_client = PyMongo(app, mongo_uri)
