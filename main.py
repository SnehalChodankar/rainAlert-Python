import requests

API_KEY = "2b85e1a21adf9ca443a2b2f59730f7d6"

parameters = {
    "lat": 29.392060,
    "lon": -98.543700,
    "cnt": 4,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
list = data["list"]
print(data)

for item in list:
    weather = item["weather"]
    weather_dict = weather[0]

    weather_id = str(weather_dict["id"])[0]
    # print(weather_id)

    if int(weather_id) < 7:
        print("Bring an Umbrella!!!")
