import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

CITIES = [
    "Pune",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad"
]

for city in CITIES:
    
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    weather_data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"data/raw/weather_{city}_{timestamp}.json"

    with open(file_path, "w") as file:
        json.dump(weather_data, file, indent=4)

    print(f"Saved: {city}")