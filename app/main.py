from flask import Flask, request, jsonify, abort, make_response, url_for
from flask_restful import Resource, Api, reqparse, fields, marshal

import config
import json

app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello world!!'}



api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
