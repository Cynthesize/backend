import datetime
from mongoengine import *

class Project(Document):
    name = StringField(max_length=200, default=None)
    category = StringField(max_length=200, default=None)
    checkpoint = StringField(max_length=200, default=None)
    comments = ListField()
    collaborators = ListField()
    description = StringField()
    is_public = BooleanField(default=False)
    owner = StringField(max_length=200, default=None)
    tags = ListField()
    upvotes = IntField(default=0)
