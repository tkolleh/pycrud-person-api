import flask
import json
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

import api.person_service as service

pycrud_person_app = Flask(__name__)
api = Api(pycrud_person_app)
CORS(pycrud_person_app)

class PersonResource(Resource):
    def get(self):
        service.get(id)


if __name__ == '__main__':
    pycrud_person_app.run(debug=True, host='localhost', port=8181) 
