from rich import print
from rich import box
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from datetime import datetime


import json
import requests


layout = Layout()
layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body")
)

layout["Body"].split_row(Layout(name = "Box1"), Layout(name = "box2"))

layout["Header"].size = 3

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Rich[/b] Layout application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")
    
layout["Header"].update(Header())

functional = "Functional"
non_functional = "Non Functional"

def Alarm():
    return Panel(f"""   _____            __                    _____ __        __            
  / ___/__  _______/ /____  ____ ___     / ___// /_____ _/ /___  _______
  \__ \/ / / / ___/ __/ _ \/ __ `__ \    \__ \/ __/ __ `/ __/ / / / ___/
 ___/ / /_/ (__  ) /_/  __/ / / / / /   ___/ / /_/ /_/ / /_/ /_/ (__  ) 
/____/\__, /____/\__/\___/_/ /_/ /_/   /____/\__/\__,_/\__/\__,_/____/  
     /____/                                                             
     
     
     
Floation 1C:    {non_functional}
Floation 1A:    {functional}
Floation 1B:    {non_functional}
Floation 1D:    {functional}

Floation 2C:    {non_functional}
Floation 2B:    {non_functional}
Floation 2A:    {functional}
Floation 2D:    {functional}

Floation 3A:    {functional}
Floation 3C:    {non_functional}
Floation 3D:    {functional}
Floation 3B:    {non_functional}

Floation 4D:    {functional}
Floation 4C:    {non_functional}
Floation 4A:    {functional}
Floation 4B:    {non_functional}

Floation 5B:    {non_functional}
Floation 5A:    {functional}
Floation 5C:    {non_functional}
Floation 5D:    {functional}""", title = "System Status", border_style = "black")
    
layout["Box1"].update(Alarm())

def Weather():

    # ---------------------------- -- - -         WORK IN PROGRESS        - -- - ----------------------------

    # ------------------------------------------  weather API  ----------------------------------------------

    api_key = "0c4d43f1d3c12b565156847bb4db7717"
    
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city_names = ["Sharjah"]


    for i in city_names:
        loop_API_output = base_url + "appid=" + api_key + "&q=" + i
    
        response = requests.get(loop_API_output)
        
        x = response.json()
        
        if x["cod"] != "404":
        
            y = x['main']
        
            loop_current_temperature = y["temp"]
        
            loop_current_pressure = y["pressure"]
        
            loop_current_humidity = y["humidity"]
        
            z = x["weather"]
        
            loop_weather_description = z[0]["description"]
        
            loop_weather_info = f" [bold red]Temperature[/bold red] (in kelvin unit) = {str(loop_current_temperature)} \n [bold red]atmospheric pressure[/bold red] (in hPa unit) =  {str(loop_current_pressure)} \n [bold red]humidity[/bold red] (in percentage) =  {str(loop_current_humidity)} \n [bold red]description[/bold red] =  {str(loop_weather_description)}"
            
            return Panel(f""" _       __           __  __                 _____ __        __            
| |     / /__  ____ _/ /_/ /_  ___  _____   / ___// /_____ _/ /___  _______
| | /| / / _ \/ __ `/ __/ __ \/ _ \/ ___/   \__ \/ __/ __ `/ __/ / / / ___/
| |/ |/ /  __/ /_/ / /_/ / / /  __/ /      ___/ / /_/ /_/ / /_/ /_/ (__  ) 
|__/|__/\___/\__,_/\__/_/ /_/\___/_/      /____/\__/\__,_/\__/\__,_/____/  
                                                                           
                                                                           
                                                                           {loop_weather_info}""", title = f"{i}", border_style = "green")
    




print(layout)