from rich import print
from rich import box
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from datetime import datetime


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
    


print(layout)