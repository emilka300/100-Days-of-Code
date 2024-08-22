##################### BIRTHDAY WISHER ######################
import random
import pandas as pd
import datetime as dt
import smtplib
import os

MY_EMAIL = "radyrradyrradyr@gmail.com"
PASSWORD = "ohnxtsgwwcqzdmgw"

# Read birthdays.csv
birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
now_month = now.month
now_day = now.day

birthday_people = pd.DataFrame()
for (index, row) in birthdays.iterrows():
    if row.month == now_month and row.day == now_day:
        birthday_people = birthday_people._append(row, ignore_index=True)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
birthday_people_dict = birthday_people.to_dict(orient="records")

for b_person in birthday_people_dict:
    lists_dir = "letter_templates"
    lists = os.listdir(lists_dir)
    list_open = open(os.path.join(lists_dir, random.choice(lists)), "r")
    list_read = list_open.read()
    birthday_list = list_read.replace("[NAME]", b_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=b_person["email"],
            msg=f"Subject:Happy birthday bitch!\n\n{birthday_list}"
        )

