from flask import Flask
from .db_config import db, ma, migrate
from dotenv import load_dotenv
import os


load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app)
    ma.init_app(app)

    return app