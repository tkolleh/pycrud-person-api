import pytest
from person_api.run import init_app
from person_api.controller import init_controller

import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join("config.ini")))


@pytest.fixture
def client():
    pycrud_person_app = init_app()

    return init_controller(pycrud_person_app)

