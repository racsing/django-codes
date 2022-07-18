import requests
import json

URL = "http://127.0.0.1:8000/student-api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    content = r.json()
    print(content)


def post_data():
    data = {
        'name': 'Ravi',
        'roll': 104,
        'city': 'bhilai',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    content = r.json()
    print(content)


def update_data():
    data = {
        'id': 4,
        'name': 'Ravinder',
        'city': 'Bilha',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    content = r.json()
    print(content)


def delete_data():
    data = {'id': 4}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    content = r.json()
    print(content)

# Method Calling
# get_data(2)
# post_data()
# update_data()
# delete_data()
