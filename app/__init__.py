from config import Config
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)
application.config.from_object(Config) # set up the config from an object we defined in config.py

socketio_handler = SocketIO(application)

webapp_db = SQLAlchemy(application)
webapp_db_migrator = Migrate(application, webapp_db)

from game_handler import GameHandler # can't import this earlier, since it requires access to webapp_db
master_game_handler = GameHandler()

from app import routes, models
