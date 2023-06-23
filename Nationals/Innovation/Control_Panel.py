from datetime import datetime
import asciichartpy
import csv
import numpy as np
import time
import math
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

layout = Layout()

layout.split_column(
    Layout(name = "Header", size = 3),
    Layout(name = "Body"),
    Layout(name = "Footer", size = 3)
)

layout["Body"].split_row(
    Layout(name = "Body_Left"),
    Layout(name = "Body_Right")
)

layout["Body_Left"].split_column(
    Layout(name = "Left_1", ratio = 1, size = 16),
    Layout(name = "Left_2")
)

layout["Body_Right"].split_column(
    Layout(name = "Right_1", size = 33, ratio = 10),
    Layout(name = "Right_2")
)

layout["Right_2"].split(
    Layout(name="R2_1", size=3),
    Layout(name="R2_2", size=3)
)

layout["Left_1"].split_row(
    Layout(name="L1_1"),
    Layout(name="L1_2", ratio = 1)
)

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Control[/b] Panel",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="blue on black")

class Footer:
    """Display footer with data."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "📝",
            "[b]Control[/b] Panel",
            "📶"
        )
        return Panel(grid, style="blue on black")

def hydro_power():
    y_values = np.random.uniform(low=0.0, high=5.0, size=10)
    Hydro_chart = asciichartpy.plot(y_values, {"height": 16, "width": 50})
    hydro_power_panel = Panel(f"{Hydro_chart}", title="Hydro energy", title_align="left", border_style="bold white", box = box.SQUARE)
    
    return hydro_power_panel

def solar_power():
    y_values = np.random.uniform(low=0.0, high=5.0, size=10)
    solar_chart = asciichartpy.plot(y_values, {"height": 16, "width": 50})
    solar_power_panel = Panel(f"{solar_chart}", title="Solar energy", title_align="left", border_style="bold white", box = box.SQUARE)
    
    return solar_power_panel

def wind_power():
    y_values = np.random.uniform(low=0.0, high=5.0, size=10)
    wind_chart = asciichartpy.plot(y_values, {"height": 10, "width": 50})
    wind_power_panel = Panel(f"{wind_chart}", title="wind energy", title_align="left", border_style="bold white", box = box.SQUARE)
    
    return wind_power_panel

def WeatherAnalysis():
    import energy_analysis as EA
    return EA.predicted_panel

def SolarOutput():
    import energy_analysis as EA
    return Panel(f"Estimated solar panel energy output: {EA.energy_output} units", title="Solar [Estimated] energy output", border_style="bold white", box = box.SQUARE)

def energy_ouput_levels():
    Solar = []
    Helical = []
    Wind = []

    for i in range(60):
        Solar.append(15 * math.cos(i * ((math.pi * 2) / 60)))  # values range from -15 to +15
        Helical.append(10 * math.sin(i * ((math.pi * 4) / 60)))  # values range from -10 to +10
        Wind.append(8 * math.sin(i * ((math.pi * 8) / 60)))  # values range from -8 to +8

    data = [Solar, Helical, Wind]
    graph = asciichartpy.plot(data, {'height': 15, 'width': 10})  # rescales the graph to ±3 lines
    return Panel(graph, border_style = "Bold white", box = box.SQUARE, title = "Energy output Analysis", title_align="left")

def solar_alerts():
    # Set a threshold for low output
    low_output_threshold = 50  # Adjust this value as needed
    
    energy_output = pre_weather.temp * (1 - pre_weather.cloud_Cover / 100) * pre_weather.uv_Index

    # Check if the output is low
    if energy_output < low_output_threshold:
        # Create an alert panel
        alert_text = "Low solar panel output!"
        alert_panel = Panel(alert_text, title="Alert", style="bold red", box=box.SQUARE)
        

        return alert_panel

    # Check if the output is sufficient
    if energy_output > low_output_threshold:
        # Create an alert panel
        alert_text = "Sufficient solar panel output 📈"
        alert_panel = Panel(alert_text, title="Solar Panel Output", style="bold green", box=box.SQUARE)
        
        return alert_panel

def wind_alerts():
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
        alert_panel = Panel(alert_text, title="Alert", style="bold red", box=box.SQUARE)
        

        return alert_panel
        
    # Check if the output is low
    if wind_power > low_output_threshold:
        # Create an alert panel
        alert_text = "Sufficient wind turbine output 📈"
        alert_panel = Panel(alert_text, title="Wid Power Output", style="bold green", box=box.SQUARE)
        

        return alert_panel

def voltage_display():
    
    title = """  _   __     ____                                   __
 | | / /__  / / /____ ____ ____   ___  _______  ___/ /
 | |/ / _ \/ / __/ _ `/ _ `/ -_) / _ \/ __/ _ \/ _  / 
 |___/\___/_/\__/\_,_/\_, /\__/ / .__/_/  \___/\_,_(_)
                     /___/     /_/                    """
    
    voltage_panel = Panel(f"{title}\n\nSolar Panels = [b green]4V[/]\nWind Turbines = [b red]2.5V[/]\nWater Turbines = [b green]3.5V[/]\n\n\n\n🚨 Alert: Enhanced Performance of Solar Panels and Water Turbines 🚨\n\n\nDue to prevailing weather conditions or unforeseen issues, we would like to inform you that the performance of our solar panels and water turbines has been notably better than that of our wind turbines. This temporary situation may affect the energy generation balance. We are actively investigating and resolving the matter. Stay tuned for updates! Thank you for your understanding. ⚡️🌊🌞111111", title="Voltage readings", border_style = "bold white", box = box.SQUARE)
    
    return voltage_panel
    
layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["Right_1"].update(voltage_display())
layout["L1_1"].update(WeatherAnalysis())
layout["L1_2"].update(SolarOutput())
layout["Left_2"].update(energy_ouput_levels())
layout["R2_1"].update(solar_alerts())
layout["R2_2"].update(wind_alerts())
print(layout)