import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://norah:1234we@localhost/safe-space'
    # API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}