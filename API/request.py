import requests

r = requests.get("http://127.0.0.1:5000/display", verify=True)
data = r.json()

for val in data:
    print (val)
