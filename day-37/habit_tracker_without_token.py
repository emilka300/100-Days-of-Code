import requests
from datetime import datetime as dt

USERNAME = "radyr"
TOKEN = ""
GRAPH_NAME = "graph1"


# CREATE ACCOUNT
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# CREATE GRAPH
graph_endpoint = F"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_NAME,
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# CREATE PIXEL
pixel_creation_endpoint = F"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_NAME}"

today = (dt.today().strftime('%Y%m%d'))
date = dt(year=2024, month=8, day=27).strftime('%Y%m%d')

pixel_config = {
    "date": today,
    "quantity": input("How many minutes have you spent on programming today? ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)


# UPDATE PIXEL
pixel_update_endpoint = F"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_NAME}/{date}"

pixel_update = {
    "quantity": "170"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)


# DELETE PIXEL
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)

