import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "Pune"

URL = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

response = requests.get(URL)

print("Status Code:", response.status_code)

weather_data = response.json()

print(json.dumps(weather_data, indent=4))