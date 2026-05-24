import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5

from config import Config
from app.extensions import db, migrate
from app.routes import main
from app.models import User

def create_app():
    app = Flask(__name__)    
    
    # Flask will copy all attributes to app.config
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    
    # Log
    logging.basicConfig(filename='logfile.txt', level = logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger('werkzeug').setLevel(logging.WARNING)
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.WARNING)
    
    # Bootstrap 5
    Bootstrap5(app)
    
    # blueprint
    app.register_blueprint(main)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app