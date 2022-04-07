import requests
from requests.auth import HTTPBasicAuth
from datetime import *

user_input = input("Tell me which exercise you did:")

# Environment Variables

APP_ID = 'your id'
APP_KEY = 'Your key'
USER = "your username"
PASS  = "your password"

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id" : "0",
    "Content-Type": 'application/json',
}

exercise_body = {
     "query": user_input
}

response = requests.post(url=exercise_endpoint, json=exercise_body, headers=headers)
workout_info = response.json()
# workout_info = workout_info["exercises"][0]
# print(workout_info["name"])
exercise_done = workout_info["exercises"][0]["name"]
exercise_duration = workout_info["exercises"][0]["duration_min"]
burned_calories = workout_info["exercises"][0]["nf_calories"]

sheet_endpoint = "https://api.sheety.co/your_spreadsheet/workoutTraining/workouts"

today = datetime.now()
now = today.time().__str__()[:8]

sheet_body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.time().__str__()[:8],
        "exercise": exercise_done.upper(),
        "duration": exercise_duration,
        "calories": burned_calories
    }
}



res = requests.post(url=sheet_endpoint, json=sheet_body, auth=(USER, PASS))
# print(res.raise_for_status())
# print(res.text)

r = requests.get(url=sheet_endpoint)
# print(r.text)
