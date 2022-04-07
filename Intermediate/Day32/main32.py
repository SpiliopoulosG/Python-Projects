import random

import pandas
import smtplib
import datetime as dt

# 1. Gets Birth dates from file
data = pandas.read_csv("birthdays.csv")
data = pandas.DataFrame.to_dict(data)

# 2. Check if today matches a birthday in the birthdays.csv
date = dt.datetime.now()
this_month = date.month
this_day = date.day


# 3. Makes Email context
def make_email_context(name):
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        email_text = file.readlines()
        email_text = ''.join(email_text)
        email_text = email_text.replace("[NAME]", f"{name}")
        return email_text


# 4. Send the letter generated in step 3 to that person's email address.
def send_email(context, receiver_email):

    my_email = "example@example.com"
    password = "App password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=f"Subject:Happy Birthday\n\n{context}")
        connection.close


# 4. Functions.
def search_birthdays():
    months = data.get("month")
    days = data.get("day")
    for key, value in months.items():
        if value == this_month:
            person_birthday_month_index = key

    for key, value in days.items():
        if value == this_day:
            person_birthday_day_index = key
    try:
        if person_birthday_month_index == person_birthday_day_index:
            return person_birthday_day_index
    except NameError:
        print("None has birthday today")


def get_email_name(index):
    name = data.get("name")
    email = data.get("email")
    return name[index], email[index]


# 6. Logic
index = search_birthdays()
if type(index) == int:
    name, email = get_email_name(index)
    email_context = make_email_context(name)
    print(email_context)
    # Uncomment to send Email after you change Email credentials
    # send_email(email_context, email)

# This works only if there are no multiples in file of birthdays ,assuming that you want to include multiples just
# append indexes to a list and send emails to each index with loop
