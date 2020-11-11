from flask import jsonify, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, abort, reqparse

from person_api.services.person import (
    get_persons,
    get_person,
    update_person_by_id,
    get_person_revision,
    remove_person_by_id,
)

_parser = reqparse.RequestParser(trim=True, bundle_errors=True)
_parser.add_argument("fname", type=str)
_parser.add_argument("mname", type=str)
_parser.add_argument("lname", type=str)
_parser.add_argument("email", type=str)
_parser.add_argument("revision", type=int)
_parser.add_argument("age", type=int)


def abort_if_not_found(person, person_id):
    if person is None:
        abort(404, message="Person with id '{}' not found".format(person_id))


class PersonListResource(Resource):
    def get(self):
        persons = get_persons()
        return jsonify(persons)


class PersonResource(Resource):
    def get(self, person_id: str):
        kargs = _parser.parse_args()
        if kargs["revision"]:
            person = get_person_revision(person_id, kargs["revision"])
        else:
            person = get_person(person_id)
        abort_if_not_found(person, person_id)
        return make_response(jsonify(person), 200)

    def put(self, person_id: str):
        kargs = _parser.parse_args()
        args = {k: v for (k, v) in kargs.items() if v}
        person = update_person_by_id(person_id, **args)
        return make_response(jsonify(person), 201)

    def delete(self, person_id: str):
        person = remove_person_by_id(person_id)
        abort_if_not_found(person, person_id)


def init_controller(app):
    CORS(app)
    api = Api(app)
    api.add_resource(PersonListResource, "/persons")
    api.add_resource(PersonResource, "/persons/<person_id>")
    return app
