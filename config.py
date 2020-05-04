from os import environ, path

config = dict()
base_url = ""
default_header = dict()
basedir = path.abspath(path.dirname(__file__))
settings_json_path = "C:/SLS_Proj1_SANA/settings.json"
processes = None


class Config(object):
    SECRET_KEY = environ.get("SECRET_KEY") or "TWICE"
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") \
        or f"sqlite:///{path.join(basedir, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
