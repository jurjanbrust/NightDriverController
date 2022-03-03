"""+===================================================================
 File:      Main.py

 NightDriverController - (c) 2021 xcalibur839. All Rights Reserved.

    NightDriverController is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
 
    NightDriverController is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with NightDriverController.  It is normally found in copying.txt
    If not, see <https://www.gnu.org/licenses/>.

 Description:

    This is a barebones controller to send color data to NightDriverStrip clients
    running on the same local network.

    Before running this file, set your configuration options in Globals.py.

    To use this program, run:
    python Main.py
    -or-
    python3 Main.py

    depending on your environment. Be sure to use Python version >= 3
===================================================================+"""

import sys
import time
from Colors import *
from Controller import *

n = len(sys.argv)
if(n > 1) :
    mode = sys.argv[1]

match mode:
    case 0:
        Controller.SetAllColor(Color.White)
    case "Red":
        Controller.SetAllColor(Color.Red)
    case "Green":
        Controller.SetAllColor(Color.Green)
    case "Blue":
        Controller.SetAllColor(Color.Blue)
    case "Gray":
        Controller.SetAllColor(Color.Gray)
    case "Wheat":
        Controller.SetAllColor(Color.Wheat)
    case "AliceBlue":
        Controller.SetAllColor(Color.AliceBlue)
    case "Aqua":
        Controller.SetAllColor(Color.Aqua)
    case "Aquamarine":
        Controller.SetAllColor(Color.Aquamarine)
    case "Azure":
        Controller.SetAllColor(Color.Azure)
    case "Beige":
        Controller.SetAllColor(Color.Beige)
    case _:
        Controller.SetAllColor(Color.White)

# Demo the AllColorCycle function
# for _ in range(5):
#     Controller.AllColorCycle(0.005)

# Demo the ColorCycle function
# for _ in range(5):
#     Controller.ColorCycle(0.001)

# # Demo the SetAllColor function
# for _ in range(5):
#     Controller.SetAllColor(Color.Red)
#     time.sleep(1)
#     Controller.SetAllColor(Color.Green)
#     time.sleep(1)
