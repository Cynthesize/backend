from mongoengine import *

class Idea(Document):
    likes = IntField(default=0)
    comments = ListField()
    owner = StringField(max_length=250, default=None)
    summary = StringField()
