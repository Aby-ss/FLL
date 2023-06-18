import json
import http.client
from rich.pretty import pprint

conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "7eafc9fb1393d7456d0778e8bde486f02bcd494f87792146729bf4e61062ae36",
    'Content-type': "application/json"
}

conn.request("GET", "/weather/forecast/by-lat-lng?lat=12.9889055&lng=77.000000574044", headers=headers)

res = conn.getresponse()
data = res.read()

json_data = data.decode("utf-8")
forecast_data = json.loads(json_data)

forecast = forecast_data["data"]["forecast"]

# Print the first entry of forecast data
print("Forecast Data:")
entry = forecast[0]
print(f"Time: {entry['time']}")
print(f"Dew Point: {entry['dewPoint']}")
print(f"Temperature: {entry['temperature']}")
print(f"Apparent Temperature: {entry['apparentTemperature']}")
print(f"Humidity: {entry['humidity']}")
print(f"Pressure: {entry['pressure']}")
print(f"Wind Speed: {entry['windSpeed']}")
print(f"Wind Bearing: {entry['windBearing']}")
print(f"Wind Gust: {entry['windGust']}")
print(f"Cloud Cover: {entry['cloudCover']}")
print(f"Visibility: {entry['visibility']}")
print(f"UV Index: {entry['uvIndex']}")
print(f"Summary: {entry['summary']}")
print(f"Icon: {entry['icon']}")
print()