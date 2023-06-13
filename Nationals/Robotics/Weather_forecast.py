import json
import http.client
from rich.pretty import pprint

from datetime import datetime
import asciichartpy
import csv
import numpy as np
import time
from time import sleep

from rich import print
from rich import box
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.layout import Layout
from rich.console import Console 

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import Progress

from rich.traceback import install
install(show_locals=True)

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
    time = entry['time']
    print(f"Dew Point: {entry['dewPoint']}")
    dew_point = entry['dewPoint']
    print(f"Temperature: {entry['temperature']}")
    temperature = entry['temperature']
    print(f"Apparent Temperature: {entry['apparentTemperature']}")
    apparent_temperature = entry['apparentTemperature']
    print(f"Humidity: {entry['humidity']}")
    humidity = entry['humidity']
    print(f"Pressure: {entry['pressure']}")
    pressure = entry['pressure']
    print(f"Wind Speed: {entry['windSpeed']}")
    wind_speed = entry['windSpeed']
    print(f"Wind Bearing: {entry['windBearing']}")
    wind_bearing = entry['windBearing']
    print(f"Wind Gust: {entry['windGust']}")
    wind_gust = entry['windGust']
    print(f"Cloud Cover: {entry['cloudCover']}")
    cloud_cover = entry['cloudCover']
    print(f"Visibility: {entry['visibility']}")
    visibility = entry['visibility']
    print(f"UV Index: {entry['uvIndex']}")
    UV_index = entry['uvIndex']
    print(f"Summary: {entry['summary']}")
    summary = entry['summary']
    print(f"Icon: {entry['icon']}")
    icon = entry['icon']
    print()
    
    print(Panel(f"Time: {time}\nDew Point: {dew_point}\nTemperature: {temperature}\nApparent Temperature: {apparent_temperature}\nHumidity: {humidity}\nPressure: {pressure}\nWind Speed: {wind_speed}\nWind Bearing: {wind_bearing}\nWind Gust: {wind_gust}\nCloud Cover: {cloud_cover}\nVisibility: {visibility}\nUV Index: {UV_index}\nSummary:{summary}"))