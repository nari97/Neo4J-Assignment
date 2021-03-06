from flask import Flask, json, request, jsonify
from flask_restful import Api, Resource
from Client import Client

app = Flask(__name__)
api = Api(app)

#Change if using different address/credentials
neo = Client("bolt://127.0.0.1:7687", "neo4j", "neo")

class Create(Resource):
    '''
        Creates employee node
    '''
    def post(self):
        data = request.form
        #print (data)
        neo.createEmployee(data["emp_name"], data["emp_id"])
        return data

class Display(Resource):
    '''
        Returns all the employees and their parameters
    '''
    def get(self):
        data = neo.returnEmployees()

        return jsonify(data)

# Add API
api.add_resource(Create, "/create")
api.add_resource(Display, "/display")

if __name__ == "__main__":
    app.run(debug = True,host = "127.0.0.1", port=5000)
