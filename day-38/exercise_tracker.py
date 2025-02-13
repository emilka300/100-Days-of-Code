import requests
from datetime import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["APP_ID"]
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 62,
    "height_cm": 164,
    "age": 25
}

# response = requests.get(url=instant_endpoint, params=parameters, headers=headers)
# print(response.text)

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
response_json = response.json()
exercise = response_json["exercises"][0]['name']
duration = response_json["exercises"][0]['duration_min']
calories = response_json["exercises"][0]['nf_calories']


# adding row to spreadsheet

today = dt.today()
date = today.strftime('%x')
time = today.strftime('%X')

new_row = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

headers_sheety = {
    "Authorization": os.environ["TOKEN"]
}

response = requests.post(url=sheety_endpoint, json=new_row, headers=headers_sheety)
response.raise_for_status()
print(response)

# deleting row from spreadsheet

# row = input("Which row? ")
#
# response = requests.delete(url=f"{sheety_endpoint}/{row}")
# response.raise_for_status()
