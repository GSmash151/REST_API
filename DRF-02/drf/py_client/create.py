# drf/py_client/create.py 

import requests

endpoint = "http://localhost:8000/api/products/"

data = {
  "title": "This field is Done!!!",
  "price": 32.99
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())