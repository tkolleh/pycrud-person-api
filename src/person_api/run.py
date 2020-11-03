import configparser
from pathlib import Path
from flask import Flask
from flask_cors import CORS
from person_api.controller import create_controller

config = configparser.ConfigParser()
config.read(Path.cwd().resolve().joinpath("config.ini"))


def init_app():

    app = Flask(__name__)
    ctx = app.app_context()
    ctx.push()
    CORS(app)
    app.config['DEBUG'] = True
    app.config['HOST'] = config['DEV']['HOST']
    app.config['PORT'] = config['DEV']['PORT']
    app.config['DB_URI'] = config['DEV']['DB_URI']
    app.config['NS'] = config['DEV']['NS']
    app.config["MAX_POOL_SIZE"] = config['DEV']['MAX_POOL_SIZE']
    app.config["WRITE_TIMEOUT"] = config['DEV']['MAX_POOL_SIZE']
    return app

if __name__ == "__main__":
    pycrud_person_app = init_app(pycrud_person_app)

    controller = create_controller(pycrud_person_app)
    controller.run()

