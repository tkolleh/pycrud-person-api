import flask
import json

from flask_restful import Resource, Api
from person_api.services.person import get_persons
from flask_cors import CORS

class PersonResource(Resource):
    def get(self):
        return get_persons()

def create_controller(app):
    CORS(app)
    api = Api(app)
    api.add_resource(PersonResource, '/person')
    return api
