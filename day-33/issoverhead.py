import requests
from datetime import datetime
import smtplib
import time

# for testing
# MY_LAT = iss_latitude+4
# MY_LNG = iss_longitude-2
MY_LAT = 51.123496
MY_LNG = 17.051007
MY_EMAIL = "radyrradyrradyr@gmail.com"
PASSWORD = "dwofavntmfpmudve"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def position():
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LNG-5 < iss_longitude < MY_LNG+5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now_hour = datetime.now().hour

# If the ISS is close to my current position
# and it is currently dark
while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    if position() is True and (sunrise >= time_now_hour or time_now_hour >= sunset):
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="emilka300@gmail.com",
                msg=f"Subject:Look up!\n\nNow you can see ISS up your head!"
            )

