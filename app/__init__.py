"""
app.py
This file is the entry point of the application.
It creates the Flask app and registers the blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from os import path
from flask_login import LoginManager
from flask import render_template

# Database variables
db = SQLAlchemy()
DB_NAME ="gcoms.db"

""" The Config class is imported from the config.py file in the project root directory """
# Create the app and pass in the configuration settings
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'mySecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # Import Models #####################################
    from .auth.auth_models import User
    from .regions.region_models import Region, City

    # Import and Register Blueprints #######################
    register_blueprints(app)


    # Create the database if it doesn't exist #################
    if not path.exists('../app/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')
    else:
        print('Database already exists!')


    # Initialize the login manager ##########################
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Invalid URL
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # Internal Server Error
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500


    # Return the app ####################################
    return app


def register_blueprints(app):
    from app.auth import bp as auth_bp
    from app.dashboard import bp as dash_bp
    from app.regions import bp as regions_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dash_bp)
    app.register_blueprint(regions_bp)

    return app



