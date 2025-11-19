import os
import requests


API_KEY = os.getenv("API_NUTRITION")
APP_ID = os.getenv("APP_ID_NUTR")
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_params = {"query": "ran for 1 hour"}

response = requests.post(url, headers=headers, json=nutrition_params)

result = response.json()
print(result["exercises"][0])
