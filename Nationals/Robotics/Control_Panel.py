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
    Layout(name = "Left_1"),
    Layout(name = "Left_2")
)

layout["Body_Right"].split_column(
    Layout(name = "Right_1"),
    Layout(name = "Right_2")
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
    #y_values = np.random.uniform(low=0.0, high=5.0, size=10)
    y_values = [10, 15, 25, 20, 25, 30, 35, 40, 45, 40, 50]    
    Hydro_chart = asciichartpy.plot(y_values, {"height": 16, "width": 50})
    hydro_power_panel = Panel(f"{Hydro_chart}", title="Hydro energy", title_align="left", border_style="bold white", box = box.SQUARE)
    
    return hydro_power_panel

def solar_power():
    #y_values = np.random.uniform(low=0.0, high=5.0, size=10)
    y_values = [10, 15, 25, 20, 25, 30, 35, 40, 45, 40, 50]    
    solar_chart = asciichartpy.plot(y_values, {"height": 16, "width": 50})
    solar_power_panel = Panel(f"{solar_chart}", title="solar energy", title_align="left", border_style="bold white", box = box.SQUARE)
    
    return solar_power_panel

def wind_power():
    #y_values = np.random.uniform(low=0.0, high=5.0, size=10)
    y_values = [10, 15, 25, 20, 25, 30, 35, 40, 45, 40, 50]    
    wind_chart = asciichartpy.plot(y_values, {"height": 16, "width": 50})
    wind_power_panel = Panel(f"{wind_chart}", title="wind energy", title_align="left", border_style="bold white", box = box.SQUARE)
    
    return wind_power_panel




layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["Left_1"].update(hydro_power())
print(layout)