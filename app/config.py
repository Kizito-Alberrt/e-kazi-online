import os

BASE_DIR =os.path.dirname(os.path.abspath(__name__))

class Config:
    '''
    General configuration parent class
    '''
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        config:The parent configuration class 
        with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config:The parent configuration class with General configuration
        settings.
    '''
    DEBUG = True