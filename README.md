Neo4J Assignment
==========================

File requirements.txt contains all the packages that are required

API
===========================

Run API/app.py to start the API. Runs on 127.0.0.1:5000.
    USE - python API/app.py

1. Create Employee Node
    API - 127.0.0.1:5000/create
    USE - curl -X POST 127.0.0.1:5000/create -d "name=test1&id=3" 

2. Display all employees
    API - 127.0.0.1:5000/display
    USE - curl 127.0.0.1:5000/display

UI
============================

Run UI/app.py. Runs on 127.0.0.1:5001
    USE - python UI/app.py

To access the homepage, type in 127.0.0.1:5001/ in the web browser.