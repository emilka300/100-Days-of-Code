import requests
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "a2e86d87edbec0395e35ad05b1469ee6"
LAT = 51.123496
mun_lat = 65.735565
LNG = 17.051007
mun_lng = 24.565742
CNT = 4
account_sid = "AC772e9e810dbcf11fc158abe681fa6f74"
auth_token = "c2ff6d693fa44e849b5af4dfe0699554"


parameters = {
    "lat": LAT,
    "lon": LNG,
    "cnt": CNT,
    "appid": API_KEY
}

will_rain = False

response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()
weather = response.json()

condition_code = weather["list"][0]["weather"][0]["id"]
weather_description = weather["list"][0]["weather"][0]["description"]
print(condition_code)
print(weather_description)

for hour_data in weather["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain is True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+18652384852',
        to='+48731170519'
    )
    print(message.status)









