# project/tests/test_user_model.py



import unittest
from mongoengine import *

from project.server.models.user_models import UserModel
from project.tests.base import BaseTestCase
from project.server.services import user_services


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = UserModel(
            username = 'username',
            email = 'test@test.com',
            password = 'test',
            first_name = 'first_name',
            last_name = 'last_name',
            gender = 'male'
        )
        user.save()
        auth_token = user_services.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = UserModel(
            username = 'username',
            email = 'test@test.com',
            password = 'test',
            first_name = 'first_name',
            last_name = 'last_name',
            gender = 'male'
        )
        user.save()
        auth_token = user_services.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

        self.assertTrue(user_services.decode_auth_token(
            auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()
