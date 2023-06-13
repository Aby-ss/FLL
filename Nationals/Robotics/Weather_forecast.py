import json
import http.client
from rich.pretty import pprint

conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "7eafc9fb1393d7456d0778e8bde486f02bcd494f87792146729bf4e61062ae36",
    'Content-type': "application/json"
}

conn.request("GET", "/weather/forecast/by-lat-lng?lat=12.9889055&lng=77.574044", headers=headers)

res = conn.getresponse()
data = res.read()

json_data = data.decode("utf-8")
forecast_data = json.loads(json_data)

forecast = forecast_data["data"]["forecast"]

for entry in forecast:
    print(f"Time: {entry['time']}")
    time = ['time']
    print(f"Dew Point: {entry['dewPoint']}")
    dew_point = ['dewPoint']
    print(f"Temperature: {entry['temperature']}")
    temperature = ['temperation']
    print(f"Apparent Temperature: {entry['apparentTemperature']}")
    apparent_temperature = ['apparentTemperature']
    print(f"Humidity: {entry['humidity']}")
    humidity = ['humidity']
    print(f"Pressure: {entry['pressure']}")
    pressure = ['pressure']
    print(f"Wind Speed: {entry['windSpeed']}")
    wind_speed = ['windSpeed']
    print(f"Wind Bearing: {entry['windBearing']}")
    wind_bearing = ['windBearing']
    print(f"Wind Gust: {entry['windGust']}")
    wind_gust = ['windGust']
    print(f"Cloud Cover: {entry['cloudCover']}")
    cloud_cover = ['cloudCover']
    print(f"Visibility: {entry['visibility']}")
    visibility = ['visibility']
    print(f"UV Index: {entry['uvIndex']}")
    UV_indox = ['uvIndex']
    print(f"Summary: {entry['summary']}")
    summary = ['summary']
    print(f"Icon: {entry['icon']}")
    icon = ['icon']
    print()