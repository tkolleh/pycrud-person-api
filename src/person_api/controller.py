from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api

from person_api.services.person import get_persons


class PersonResource(Resource):
    def get(self):
        persons = get_persons()
        persons = [p.to_json() for p in persons]
        return persons

    def put(self, person_id: str):
        payload = request.json


def init_controller(app):
    CORS(app)
    api = Api(app)
    api.add_resource(PersonResource, "/person")
    return app
