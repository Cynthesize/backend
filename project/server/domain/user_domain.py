# /usr/bin/env python3

import datetime
# from project.server import app, bcrypt
from project.server.models import user_models


class UserDomain(object):
    """Domain object for UserModel"""
    
    def __init__(self, id, username, password, email, first_name, last_name,
        gender, contact_number, profile_picture, organisation,
        subscription):
        """Function that initialises the UserModel."""

        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.contact_number = contact_number
        self.profile_picture = profile_picture
        self.organisation = organisation
        self.joined_on = datetime.datetime.now()
        self.subscription = subscription
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'contact_number': self.contact_number,
            'profile_picture': self.profile_picture,
            'organisation': self.organisation,
            'joined_on': self.joined_on,
            'subscription': self.subscription             
        }
