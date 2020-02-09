import os

class Config(object):
    DEBUG = False
    TESTING = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Leonardo.130.@localhost/pirotech"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    JWT_SECRET_KEY = '3ae03a298434a5a187b3d6a52360853b3c18b2cf4b3828f0'
    ENV = 'development'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Leonardo.130.@localhost/pirotech_test"

