import requests
from datetime import datetime as dt
MY_LAT = 51.107883
MY_LNG = 17.038538

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # print(response.text)
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# print(longitude)
#
# latitude = data["iss_position"]["latitude"]
# print(latitude)
#
# iss_position = (longitude, latitude)
# print(iss_position)


# option with paramteters
# parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
# response = requests.get(url=f"https://api.sunrise-sunset.org/json", params= parameters)
# option with changed url
response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)

time_now = dt.now().hour
print(time_now)
