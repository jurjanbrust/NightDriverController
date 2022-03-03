"""+===================================================================
 File:      Globals.py

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

    Specify the list of client IP addresses in CLIENTS and the number of LEDs in
    LED_COUNT. Currently all clients must have the same number of LEDs.
===================================================================+"""

# Do not modify these values unless you know what you're doing
COMMAND_ID = 3
CHANNEL_ID = 1
ENDIANNESS = "little"

# Modify these values based on your specific hardware and network setup
LED_COUNT = 505
CLIENTS = [
    "192.168.1.253"
]   