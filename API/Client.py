from neo4j import GraphDatabase
from neo4j.work.simple import Session
import json

class Client:
    
    def __init__(self, url, user, password) -> None:
        self.driver = GraphDatabase.driver(url, auth = (user, password))

    def createEmployee(self, name, id):
        '''
            Creates employee

            Input
            ==========
            
            name (str): Name of employee
            id (int): ID of employee

            Returns
            ==========

            JSON containing name and id
        '''

        session = self.driver.session()
        session.run("CREATE (e:Employee {name:$name, emp_id:$emp_id})", name = name, emp_id = id)
        session.close()

        return json.dumps({'name' : name, 'emp_id' : id})

    def returnEmployees(self):
        '''
            Returns all employees

            Returns
            ==========

            List containing employee details
        '''

        session = self.driver.session()
        result = session.run("MATCH (e:Employee) RETURN e.name AS name, e.emp_id AS id")

        data = []
        for row in result:
            #print (row["name"])
            data.append({"name" : row['name'], "emp_id" : row['id']})
        session.close()

        return data


    def close(self):
        '''
            Close connection with database
        '''
        self.driver.close()

