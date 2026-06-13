import requests

from config import (
    API_KEY,
    CITIES,
    BASE_URL
)

from utils import save_json


for city in CITIES:

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        BASE_URL,
        params=params
    )

    if response.status_code == 200:

        weather_data = response.json()

        file_path = save_json(
            weather_data,
            city
        )

        print(
            f"SUCCESS: {city} -> {file_path}"
        )

    else:

        print(
            f"FAILED: {city}"
        )