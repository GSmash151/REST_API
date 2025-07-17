# drf/py_client/list.py

import requests
from getpass import getpass

# Auth Endpoint
auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your Name: ")
password = getpass("What is your Password: ")

auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password}
)

if auth_response.status_code == 200:
    token = auth_response.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}

    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
else:
  print(f"Authentication failed with status code{auth_response.status_code}.")
