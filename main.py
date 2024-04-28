import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


API_KEY = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": 15.645460,
    "lon": 73.828033,
    "cnt": 4,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
list_data = data["list"]
print(data)


will_rain = False
for item in list_data:
    weather = item["weather"]
    weather_dict = weather[0]

    weather_id = str(weather_dict["id"])[0]
    # print(weather_id)

    if int(weather_id) < 7:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its going to rain, bring an umbrella",
        from_='+17193575948',
        to='+919284832649'
    )

    print(message.status)
else:

    print("Its not raining today!!!")