from flask import request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, abort
from person_api.services.person import get_persons, get_person, new_person


class PersonListResource(Resource):
    def get(self):
        persons = get_persons()
        return jsonify(persons)


class PersonResource(Resource):
    def get(self, person_id: str):
        person = get_person(person_id)
        if person is None:
            abort(404, message="Person with id '{}' not found".format(person_id))
        return jsonify(person)

    def put(self, person_id: str):
        payload = request.json
        new_person(payload['fname'], payload['mname'], payload['lname'], payload['email'], payload['age'])


def init_controller(app):
    CORS(app)
    api = Api(app)
    api.add_resource(PersonListResource, "/persons")
    api.add_resource(PersonResource, "/persons/<person_id>")
    return app
