import os
import requests
from datetime import datetime

API_KEY = os.getenv("API_NUTRITION")
APP_ID = os.getenv("APP_ID_NUTR")
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = os.getenv("END_POINT")


headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")
prop = {"email": {"name": "Kevin", "email": "test@gmail.com"}}

nutrition_params = {"query": "ran for 1 hour"}

response = requests.post(url, json=nutrition_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
    print(sheet_response.text)
