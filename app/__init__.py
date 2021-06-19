from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

#instances of flask extensions
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
mail = Mail()
#initialize application
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app=Flask(__name__)

    simple.init_app(app) 

    # creating app configurations 
    app.config.from_object(config_options[config_name])
    

from app import views 