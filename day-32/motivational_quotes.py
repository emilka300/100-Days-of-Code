import random
import datetime as dt
import smtplib

MY_EMAIL = "radyrradyrradyr@gmail.com"
PASSWORD = "ohnxtsgwwcqzdmgw"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    f = open("quotes.txt.", "r")
    quotes = f.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # starttls() - encrypts email - secure connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="emilka300@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{random.choice(quotes)}"
        )

