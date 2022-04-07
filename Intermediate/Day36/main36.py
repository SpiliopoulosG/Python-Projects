import requests
from twilio.rest import Client


MY_LAT = 37.934553
MY_LONG = 23.725167
account_sid = 'Your ACC_ID'
auth_token = 'Your Auth_token'
api_id = "Your_Api"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "APPID": api_id,
    'exclude': "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It is going to rain Today, Remember to bring an umbrella", from_="+17623025600",
                to="+306987508001")
    print(message.status)
