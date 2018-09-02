# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
connection_url = 'mongodb://wickedbrat:123@localhost/startup'
database_name = 'startup'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    MONGO_CONNECTION_URI = connection_url + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    MONGO_CONNECTION_URI = connection_url + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    MONGO_CONNECTION_URI = 'postgresql:///example'
