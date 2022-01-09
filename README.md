Neo4J Assignment
==========================

File requirements.txt contains all the packages that are required
    
    pip install -r requirements.txt

API
===========================

Run API/app.py to start the API. Runs on 127.0.0.1:5000.

    python API/app.py

1. Create Employee Node

    API - 127.0.0.1:5000/create
    
    USE - curl -X POST 127.0.0.1:5000/create -d "name=test1&id=3" 

2. Display all employees

    API - 127.0.0.1:5000/display
    
    USE - curl 127.0.0.1:5000/display

UI
============================

Run UI/app.py. Runs on 127.0.0.1:5001. Make sure to also run API/app.py before running UI/app.py

    python UI/app.py

To access the homepage, type in 127.0.0.1:5001/ in the web browser.
