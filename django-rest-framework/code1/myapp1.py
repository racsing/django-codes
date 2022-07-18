# Third party APP

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

# python object
data = {
    'name': 'rohit',
    'roll': 106,
    'city':'Bhilai',
}
info = json.dumps(data)     # python object to json
print(info)

res = requests.post(url=URL, data=info)     # post request

mydata = res.json()
print(mydata)