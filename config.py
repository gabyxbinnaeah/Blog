import os 

class Config:
    '''
    a method that provides general settings for application
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:silfanus12@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
      # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

      #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Method that provides configuration  setting for production

    Args: 
         Permits child class to inherit from class Config
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass
class DevConfig(Config):
    '''
    Method that sets configuarations for development class
    Args: 
         enable child class to inherit from parent class 
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:silfanus12@localhost/blog' 

    DEBUG=True



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}