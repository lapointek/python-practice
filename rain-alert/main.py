import requests

api_key = "5fe1bb085f9b36f7607cb07c7436a1b2"

lat = 43.65
lng = -79.38

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
)

response_json = response.json()
response_status = response.status_code
print(response_status)
