
import requests

from pprint import pprint
from datetime import datetime

API = "3366c6b7a4d7493d05000bf25b485dbe"

def weather_city(API, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    response = requests.get(url)
    data = response.json()

    sunrise = datetime.fromtimestamp(data["sys"] ["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"] ["sunset"])

    return f"""

Город: {data["name"]}
Температура: {data["main"]["temp"]}
Давление: {data["main"]["pressure"]}
Влажность: {data["main"]["humidity"]}
Скорость ветра: {data["wind"]["speed"]}

Погода: {data["weather"][0]["description"]}
Восход солнца: {sunrise.time()}
Продолжительность дня: {sunset - sunrise}
Продолжительность ночи: {sunrise - sunset}
Закат солнца: {sunset.time()}

"""
while True:
    try:
        city = input("Введите город: ")
        API = "3366c6b7a4d7493d05000bf25b485dbe"
        print(weather_city(API, city))
        break
    except Exception:
        print("Такого города нет ")
        break







