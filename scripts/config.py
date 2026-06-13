import os
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

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"