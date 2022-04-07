import requests
from datetime import datetime
import smtplib
import time

my_email = "example@com" # Your email
password = "passphrase" # Your passphrase

MY_LAT = 37.934553
MY_LONG = 23.725167

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

today = datetime.now()

while True:
    time.sleep(60)
    # If the ISS is close to my current position
    ISS_OVER_ME = False
    IS_NIGHT = False
    if MY_LONG - 5 < iss_longitude < MY_LONG + 5 and MY_LAT - 5 < iss_latitude < MY_LAT + 5 :
        ISS_OVER_ME = True
    # and it is currently dark
    if  16 < today.hour or today.hour < 4:
        IS_NIGHT = TRUE
    # Then send me an email to tell me to look up.
    if IS_NIGHT is True and ISS_OVER_ME is True:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="example@example.com", msg=f"Subject:ISS Reminder\n\nISS is above you!")
            connection.close




