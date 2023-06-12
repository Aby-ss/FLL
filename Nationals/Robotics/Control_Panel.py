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

print(layout)