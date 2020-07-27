"""
Use configurations folder to store all configurations related data
"""

import os

class Config(object):
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Production'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}
    JWT_BLACKLIST_ENABLED = True  # enable blacklist feature
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    # MAIL_USE_TLS = bool(os.getenv('MAIL_USE_TLS'))
    MAIL_USE_SSL = bool(os.getenv('MAIL_USE_SSL')) 
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_ASCII_ATTACHMENTS = bool(os.getenv('MAIL_ASCII_ATTACHMENTS'))
    DEFAULT_MAIL_SENDER = os.getenv('DEFAULT_MAIL_SENDER')


class Development(Config):
    ENVIRONMENT = 'Development'
    DEBUG = True
    MAIL_DEBUG = True
   
class Testing (Config):
    ENVIRONMENT = 'Production'
    DEBUG = False
    MAIL_DEBUG = False

    
class Production(Config):
    ENVIRONMENT = 'Production'
    DEBUG = False
    MAIL_DEBUG = False

