import datetime
import pymongo
from mongoengine import *

class UserModel(Document):
    email = StringField(required=True, default=None)
    ideas_contributed = ListField()
    last_login = DateTimeField(auto_now=True)
    number_of_login = IntField(default=0)
    profile_picture = StringField(max_length=250, default=None)
    projects_owned = ListField()
    projects_contributed = ObjectIdField()
    projects_in_review = ListField()
    generates_revenue = ListField()
    location = StringField(max_length=250, default=None)
    organisation = StringField(max_length=250, default=None)
    skills_known = ListField()
    subscription = BooleanField(default=True)
