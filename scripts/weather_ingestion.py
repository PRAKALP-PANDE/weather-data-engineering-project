import requests
from datetime import datetime, timezone

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

        timestamp = datetime.now(timezone.utc)

        weather_data["ingestion_timestamp"] = timestamp.isoformat()

        file_path = save_json(
            weather_data,
            city,
            timestamp
        )

        print(
            f"SUCCESS: {city} -> {file_path}"
        )

    else:

        print(
            f"FAILED: {city}"
        )