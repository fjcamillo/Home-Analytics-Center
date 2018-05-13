from flask import Flask
from flask-sqlalchemy import SQLAlchemy
from flask-migrate import Migrate


app = Flask(__name__)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import app