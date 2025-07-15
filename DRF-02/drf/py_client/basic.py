import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello Chuck"}) # HTTP Request
print(get_response.text) # prints out the raw text response code


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
print(get_response.json())

# 
# https://youtu.be/c708Nf0cHrs?t=1706