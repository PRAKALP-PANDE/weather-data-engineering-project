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

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

file_path = f"data/raw/weather_{CITY}_{timestamp}.json"

with open(file_path, "w") as file:
    json.dump(weather_data, file, indent=4)

print(f"Data saved to {file_path}")