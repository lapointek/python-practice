import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "5fe1bb085f9b36f7607cb07c7436a1b2"

weather_params = {
    "lat": 43.65,
    "lon": -79.38,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())
