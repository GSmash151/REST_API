# drf/py_client/update.py

import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
  "title": "Hello Ganil my old friend",
  "price": 129.99
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())