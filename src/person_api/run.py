import configparser
from pathlib import Path

from flask import Flask
from flask_cors import CORS

from person_api.controller import init_controller
from person_api.db import init_db

config = configparser.ConfigParser()
config.read(Path.cwd().resolve().joinpath("config.ini"))


def init_app():
    app = Flask(__name__)
    ctx = app.app_context()
    ctx.push()
    app.config["DEBUG"] = config["WEBSERVER"].getboolean("DEBUG")
    app.config["HOST"] = config["WEBSERVER"]["HOST"]
    app.config["PORT"] = config["WEBSERVER"]["PORT"]
    app.config["MONGODB_SETTINGS"] = {
        "db": config["MONGODB_SETTINGS"]["DB"],
        "host": config["MONGODB_SETTINGS"]["HOST"],
        "maxpoolsize": config["MONGODB_SETTINGS"]["MAX_POOL_SIZE"],
        "connect": config["MONGODB_SETTINGS"]["CONNECT"],
    }
    return app


if __name__ == "__main__":
    pycrud_person_app = init_app()
    init_db(pycrud_person_app)
    CORS(pycrud_person_app)
    init_controller(pycrud_person_app).run()
