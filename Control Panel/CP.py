from rich import print
from rich import box
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

from rich.traceback import install
install(show_locals=True)


from bs4 import BeautifulSoup
import requests


layout = Layout()
layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body")
)

layout["Body"].split_row(Layout(name = "Box1"), Layout(name = "Box2"))
layout["Box2"].split(Layout(name = "Weather"), Layout(name = "Energy Production Levels"))


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Control[/b] Panel application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="blue on black")
    

functional = "Functional"
non_functional = "Non Functional"

def Alarm():
    return Panel(f"""
   _____            __                         __        __            
  / ___/__  _______/ /____  ____ ___     _____/ /_____ _/ /___  _______
  \__ \/ / / / ___/ __/ _ \/ __ `__ \   / ___/ __/ __ `/ __/ / / / ___/
 ___/ / /_/ (__  ) /_/  __/ / / / / /  (__  ) /_/ /_/ / /_/ /_/ (__  ) 
/____/\__, /____/\__/\___/_/ /_/ /_/  /____/\__/\__,_/\__/\__,_/____/  
     /____/                                                            
        
        
    Floation 1C:   [b red]{non_functional}[/]
    Floation 1A:   [b green]{functional}[/]
    Floation 1B:   [b red]{non_functional}[/]
    Floation 1D:   [b green]{functional}[/]

    Floation 2C:   [b red]{non_functional}[/]
    Floation 2B:   [b red]{non_functional}[/]
    Floation 2A:   [b green]{functional}[/]
    Floation 2D:   [b green]{functional}[/]

    Floation 3A:   [b green]{functional}[/]
    Floation 3C:   [b red]{non_functional}[/]
    Floation 3D:   [b green]{functional}[/]
    Floation 3B:   [b red]{non_functional}[/]

    Floation 4D:   [b green]{functional}[/]
    Floation 4C:   [b red]{non_functional}[/]
    Floation 4A:   [b green]{functional}[/]
    Floation 4B:   [b red]{non_functional}[/]

    Floation 5B:   [b red]{non_functional}[/]
    Floation 5A:   [b green]{functional}[/]
    Floation 5C:   [b red]{non_functional}[/]
    Floation 5D:   [b green]{functional}[/]""", title = "System Status", border_style = "black")


def energy_levels():
    energy_levels_panel = Panel("""
                  Water
            ┌────────────────────────────────────────┐
            │                                        │
            │      +++      +        +++             │
            │     ++++++    ++      +++++            │----------- [b green]Good[/]
            │    +++++++   ++++   ++++++++++++++     │
            │+++++++++++++++++++++++++++++++++++++   │
            └────────────────────────────────────────┘
                  Solar
            ┌────────────────────────────────────────┐
            │      +++                               │
            │     +++++              ++++            │
            │    +++++++     +++    +++++     +   +++│----------- [b yellow]Average[/]
            │    ++++++++  ++++++  ++++++++  +++  +  │
            │  ++++++++++++++++++++++++++++++++++++  │
            └────────────────────────────────────────┘
                  Wind
            ┌────────────────────────────────────────┐
            │       +++        ++++                  │
            │     ++++++      ++++++       ++        │
            │    ++++++++    ++++++++     ++++    ++ │----------- [b green]Great[/]
            │   +++++++++   ++++++++++   ++++++  +++ │
            │  +++++++++++++++++++++++++++++++++++++ │
            └────────────────────────────────────────┘
                                
                                """, title = "Energy Production Levels", subtitle = "Solar  Wind  Water", subtitle_align = "left", title_align = "left", border_style = "bold green")
    
    return energy_levels_panel


layout["Header"].size = 3
layout["Energy Production Levels"].ratio = 2
layout["Energy Production Levels"].update(energy_levels())
layout["Box1"].update(Alarm())
layout["Header"].update(Header())

print(layout)