import json
import os

def save_json(data, city, timestamp):
    file_timestamp = timestamp.strftime(
        "%Y%m%d_%H%M%S"
    )

    dir_path = f"data/raw/{city}"
    file_path = f"{dir_path}/{file_timestamp}.json"

    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return file_path
