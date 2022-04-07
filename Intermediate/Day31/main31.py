import smtplib
import datetime as dt
import random

my_email = "example@example.com"
password = "App password"


# Sends Motivational Quote every Monday
day =dt.datetime.now()
if day.weekday() == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        # print(random.choice(lines))


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="example@example.com", msg=f"Subject:Quote of the Week\n\n{random.choice(quotes)}")
        connection.close



