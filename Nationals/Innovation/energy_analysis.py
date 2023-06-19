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

import Weather_forecast as pre_weather

predicted_panel = Panel(f"[b]Time: [/]{pre_weather.time}\n[b]Dew Point: [/]{pre_weather.dewPoint}\n[b]Temperature: [/]{pre_weather.temp}\n[b]Apparent Temperature: [/]{pre_weather.app_temp}\n[b]Humidity: [/]{pre_weather.humidity}\n[b]Atmsopheric Pressure: [/]{pre_weather.pressure}\n[b]Wind Speed: [/]{pre_weather.wind_speed}\n[b]Wind Bearing: [/]{pre_weather.Wind_bearing}\n[b]Wind Gust: [/]{pre_weather.wind_Gust}\n[b]Cloud Cover: [/]{pre_weather.cloud_Cover}\n[b]Visibility: [/]{pre_weather.visibility}\n[b]UV Index: [/]{pre_weather.uv_Index}\n[b]Summary: [/]{pre_weather.summary}\n[b]Weather Icon: [/]{pre_weather.weather_icon}", title="Predicted Weather", border_style="bold white", box = box.SQUARE)
print(predicted_panel)