import json
from datetime import datetime


def save_json(data, city):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"data/raw/weather_{city}_{timestamp}.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return file_path