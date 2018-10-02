from flask import Flask, request, jsonify, abort, make_response, url_for
from flask_restful import Resource, Api, reqparse, fields, marshal
import pyodbc
import config
import json

app = Flask(__name__)
api = Api(app)

sampleTable_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'value': fields.String
}

dataTable_fields = {
    'id': fields.Integer,
    'datavalue': fields.Integer
}

class AzureSQLDatabase(object):
    connection = None
    cursor = None

    def __init__(self):
        self.connection = pyodbc.connect(config.CONN_STRING)
        self.cursor = self.connection.cursor()

    def query(self, query):
        return self.cursor.execute(query)
    
    def commit(self):
        return self.connection.commit()
    
    def __del__(self):
        self.connection.close()

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello world!!'}

class HelloWorldv2(Resource):
    def get(self):
        try:
            sql = u"select * from sampleTable"
            conn = AzureSQLDatabase()
            cursor = conn.query(sql)
            columns = [column[0] for column in cursor.description]
            data = []
            for row in cursor.fetchall():
                data.append(dict(zip(columns, row)))

            return {
                'data': marshal(data, sampleTable_fields)
            }
        except Exception as e:
            return {'error': str(e)}


class Testv2(Resource):
    def get(self):
        try:
            sql = u"select * from dataTable"
            conn = AzureSQLDatabase()
            cursor = conn.query(sql)
            columns = [column[0] for column in cursor.description]
            data = []
            for row in cursor.fetchall():
                data.append(dict(zip(columns, row)))

            return {
                'data': marshal(data, dataTable_fields)
            }
        except Exception as e:
            return {'error': str(e)}

api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorldv2, '/api/v1/test')
api.add_resource(Testv2, '/api/v1/test2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
