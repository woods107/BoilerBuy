from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
# database instance handlers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager
# include models to organize dbs
from app import routes, models
