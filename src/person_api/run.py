import configparser
from pathlib import Path

from flask import Flask, current_app
from flask_cors import CORS

from person_api.controller import init_controller
from person_api.db import init_db


def init_app():
    config = configparser.ConfigParser()
    config.read(Path.cwd().resolve().joinpath("config.ini"))
    print("TRACE: Current config sections include: \n{}".format(config.sections()))

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


def create_app():
    app = init_app()
    init_db(app)
    CORS(app)
    app = init_controller(app)
    return app


if __name__ == "__main__":
    pycrud_person_app = init_app()
    init_db(pycrud_person_app)
    CORS(pycrud_person_app)
    init_controller(pycrud_person_app).run(
        debug=current_app.config["DEBUG"],
        host=current_app.config["HOST"],
        port=current_app.config["PORT"],
    )
