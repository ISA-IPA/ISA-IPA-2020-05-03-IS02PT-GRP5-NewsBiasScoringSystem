from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
# from logging.handlers import RotatingFileHandler
# import logging

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

from app import routes, models

# if not app.debug:
#     file_handler = RotatingFileHandler("./logs/app.log", maxBytes=10240,
#                                        backupCount=10)
#     file_handler.setFormatter(logging.Formatter(
#         "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
#     ))
#     file_handler.setLevel(logging.INFO)
#
#     app.logger.setLevel(logging.INFO)
#     app.logger.info("Application startup")
