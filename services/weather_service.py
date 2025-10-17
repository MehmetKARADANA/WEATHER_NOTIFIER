import requests
from config import OPENWEATHER_API_KEY, DEFAULT_CITY

def get_weather(city: str = DEFAULT_CITY):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
