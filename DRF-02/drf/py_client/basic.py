import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"product_id": 123}) # HTTP Request
print(get_response.headers)
print(get_response.text) # prints out the raw text response code
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
# print(get_response.json())
# print(get_response.status_code)

