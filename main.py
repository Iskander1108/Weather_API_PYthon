#16.08.23 


# import requests

# from pprint import pprint
# from datetime import datetime

# API = "3366c6b7a4d7493d05000bf25b485dbe"
# city = "Almaty"

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

# response = requests.get(url)

# data = response.json()

# # pprint(data)

# sunrise = datetime.fromtimestamp(data["sys"] ["sunrise"])
# sunset = datetime.fromtimestamp(data["sys"] ["sunset"])

# info = f"""

# Город: {data["name"]}
# Температура: {data["main"]["temp"]}
# Давление: {data["main"]["pressure"]}
# Влажность: {data["main"]["humidity"]}
# Скорость ветра: {data["wind"]["speed"]}

# Погода: {data["weather"][0]["description"]}
# Восход солнца: {sunrise.time()}
# Продолжительность дня: {sunset - sunrise}
# Продолжительность ночи: {sunrise - sunset}
# Закат солнца: {sunset.time()}

# """

# print(info)










