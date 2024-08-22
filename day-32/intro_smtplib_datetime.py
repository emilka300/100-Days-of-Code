import smtplib
import datetime as dt

my_email = "radyrradyrradyr@gmail.com"
# password is created in app passwords in profile of account
password = "ohnxtsgwwcqzdmgw"

# this way with "with ... as connection" we dont have to write: connection.close() at the end
# smtplib.SMTP("smtp.gmail.com") server's smtp it's different each time we change platform where is from the sender
with smtplib.SMTP("smtp.gmail.com") as connection:
    # starttls() - encrypts email - secure connection
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="emilka300@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

# current date and time -> .now()
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)

date_of_birth = dt.datetime(year=1999, month=5, day=17)
print(date_of_birth)
