# project/server/models.py

from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField


class UserModel(Document):
    """ User Model for storing user related details """

    id = StringField(required=True, max_length=250)
    username = StringField(required=True, max_length=250)
    password = StringField(max_length=250)
    email = StringField(required=True, default=None)
    first_name = StringField(required=True, max_length=250)
    last_name = StringField(required=True, max_length=250)
    gender = StringField(required=True, max_length=10)
    contact_number = IntField(max_length=250)
    profile_picture = StringField(max_length=250, default=None)
    organisation = StringField(max_length=250, default=None)
    subscription = BooleanField(default=True)
    joined_on = DateTimeField()


# class WhitelistedTokensModel(Document):
#     """Token Model for storing JWT tokens."""

#     id = StringField(required=True, max_length=250)
#     user_id = StringField(required=True, max_length=250)
#     token = StringField(required=True, max_length=250)

#     def __init__(self, user_id, token):
#         self.user_id = user_id
#         self.token = token

#     def __repr__(self):
#         return '<id: token: {}'.format(self.token)

#     @staticmethod
#     def check_whitelist(auth_token):
#         # check whether auth token has been blacklisted
#         for tokens in WhitelistedTokensModel.objects:
#             if tokens.token = 