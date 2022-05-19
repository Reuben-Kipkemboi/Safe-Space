import os
class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/dbsafe'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# class TestConfig(Config):

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://lqxssqojjiudkb:98705d02848004c95ff66533c98eaf6c171547a2b6adc96f98a36c5d0ba91cf8@ec2-54-204-56-171.compute-1.amazonaws.com:5432/da27vsvg57ieid'

class DevConfig(Config):
    pass
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,

}