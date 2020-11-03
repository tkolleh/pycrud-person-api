import pytest
from person_api.run import init_app
from person_api.controller import init_controller
from person_api.db import init_db

import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join("config.ini")))


@pytest.fixture
def client():
    pycrud_person_app = init_app()
    init_db(pycrud_person_app)
    return init_controller(pycrud_person_app)
