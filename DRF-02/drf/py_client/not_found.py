import requests

endpoint = "http://localhost:8000/api/products/164846184545468/"

get_response = requests.get(endpoint)
print(get_response.json())