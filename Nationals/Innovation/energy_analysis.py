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

predicted_panel = Panel.fit(f"[b]Time: [/]{pre_weather.time}\n[b]Dew Point: [/]{pre_weather.dewPoint}\n[b]Temperature: [/]{pre_weather.temp}\n[b]Apparent Temperature: [/]{pre_weather.app_temp}\n[b]Humidity: [/]{pre_weather.humidity}\n[b]Atmsopheric Pressure: [/]{pre_weather.pressure}\n[b]Wind Speed: [/]{pre_weather.wind_speed}\n[b]Wind Bearing: [/]{pre_weather.Wind_bearing}\n[b]Wind Gust: [/]{pre_weather.wind_Gust}\n[b]Cloud Cover: [/]{pre_weather.cloud_Cover}\n[b]Visibility: [/]{pre_weather.visibility}\n[b]UV Index: [/]{pre_weather.uv_Index}\n[b]Summary: [/]{pre_weather.summary}\n[b]Weather Icon: [/]{pre_weather.weather_icon}", title="Predicted Weather", border_style="bold green", box = box.SQUARE)
print(predicted_panel)

# Calculate solar panel energy output
energy_output = pre_weather.temp * (1 - pre_weather.cloud_Cover / 100) * pre_weather.uv_Index

Estimate_solar_output = Panel.fit(f"Estimated solar panel energy output: {energy_output} units", border_style="bold green", box = box.SQUARE)
print(Estimate_solar_output)


def solar_analysis():
    
    # Set a threshold for low output
    low_output_threshold = 50  # Adjust this value as needed
    
    energy_output = pre_weather.temp * (1 - pre_weather.cloud_Cover / 100) * pre_weather.uv_Index
    
    # Check if the output is low
    if energy_output < low_output_threshold:
        # Create an alert panel
        alert_text = "Low solar panel output!"
        alert_panel = Panel.fit(alert_text, title="Alert", style="bold red", box=box.SQUARE)
        

        return alert_panel

    # Check if the output is sufficient
    if energy_output > low_output_threshold:
        # Create an alert panel
        alert_text = "Sufficient solar panel output 📈"
        alert_panel = Panel.fit(alert_text, title="Solar Panel Output", style="bold green", box=box.SQUARE)
        
        return alert_panel
        
solar_analysis()

# Calculate wind turbine energy output
rotor_diameter = 50  # Adjust this value for your wind turbine
air_density = 1.225  # Adjust this value for your location
wind_speed = pre_weather.wind_speed  # Wind speed is provided in the pre_weather data
    
# Calculate wind power using the formula: P = 0.5 * air_density * A * v^3
wind_power = 0.5 * air_density * np.pi * (rotor_diameter/2)**2 * wind_speed**3
print(Panel.fit(f"{wind_power}", title="Wind Power", border_style="bold white"))

def Wind_analysis():    
    # Calculate wind turbine energy output
    rotor_diameter = 50  # Adjust this value for your wind turbine
    air_density = 1.225  # Adjust this value for your location
    wind_speed = pre_weather.wind_speed  # Wind speed is provided in the pre_weather data
    
    wind_power = 0.5 * air_density * np.pi * (rotor_diameter/2)**2 * wind_speed**3


    # Set a threshold for low output
    low_output_threshold = 1000000  # Adjust this value as needed

    # Check if the output is low
    if wind_power < low_output_threshold:
        # Create an alert panel
        alert_text = "Low wind turbine output!"
        alert_panel = Panel.fit(alert_text, title="Alert", style="bold red", box=box.SQUARE)
        

        return alert_panel
        
    # Check if the output is low
    if wind_power > low_output_threshold:
        # Create an alert panel
        alert_text = "Sufficient wind turbine output 📈"
        alert_panel = Panel.fit(alert_text, title="Wid Power Output", style="bold green", box=box.SQUARE)
        

        return alert_panel

Wind_analysis()