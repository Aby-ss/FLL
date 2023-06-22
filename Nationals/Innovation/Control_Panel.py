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
    Layout(name = "Right_1", size = 25, ratio = 10),
    Layout(name = "Right_2")
)

layout["Right_2"].split(
    Layout(name="R2_1"),
    Layout(name="R2_2")
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
            "🗺",
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
    import energy_analysis as EA
    EA.solar_analysis()

layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["L1_1"].update(WeatherAnalysis())
layout["L1_2"].update(SolarOutput())
layout["Left_2"].update(energy_ouput_levels())
layout["R2_1"].update(solar_alerts())
layout["R2_2"].update()
print(layout)