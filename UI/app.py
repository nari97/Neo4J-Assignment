from flask import Flask, jsonify, request
from flask import render_template

import requests
#from Client.Client import Client

app = Flask(__name__)

#Homepage
@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('main.html')    

#Enter data to create employee node
@app.route("/enterdata", methods = ["GET"])
def enterdata():
    return render_template('enterdata.html')
    
#Creates employee node
@app.route("/create", methods = ["GET", "POST"])
def create():
    form = request.form
    
    data = form.to_dict()
    requests.post("http://127.0.0.1:5000/create", data = data)
    return render_template('main.html')

#Displays employees
@app.route("/display", methods = ["GET"])
def display():
    data = requests.get("http://127.0.0.1:5000/display").json()
    #print (data)
    return render_template('displayemployees.html', data = data)


if __name__ == "__main__":
    app.run(debug=True,host = "127.0.0.1",port=5001)

