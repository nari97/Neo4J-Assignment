from flask import Flask, json, request, jsonify
from flask_restful import Api, Resource
from Client import Client

app = Flask(__name__)
api = Api(app)

#Connect to Neo4J
neo = Client("bolt://127.0.0.1:7687", "neo4j", "neo")

#API to create employee
class Create(Resource):
    def post(self):
        data = request.form
        #print (data)
        neo.createEmployee(data["emp_name"], data["emp_id"])
        return data

#API to display all employees
class Display(Resource):
    def get(self):
        data = neo.returnEmployees()

        return jsonify(data)

api.add_resource(Create, "/create")
api.add_resource(Display, "/display")

if __name__ == "__main__":
    app.run(debug = True,host = "127.0.0.1", port=5000)
