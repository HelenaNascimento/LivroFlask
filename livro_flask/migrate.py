from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_active, app_config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    config = app_config[app_active]
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Importar os modelos para que o Flask-Migrate os reconheça
    from models import Role, User, Category, Product

    return app
