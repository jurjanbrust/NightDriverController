"""+===================================================================
 File:      Controller.py

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

    This file contains all of the logic for building and sending packets to
    clients. All members are static, no instantiation required.
===================================================================+"""

import socket, Globals

class Controller:
    __clients = []
    for client in Globals.CLIENTS:
        __clients.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        __clients[-1].connect((client, 49152))

    # SetAllColor
    #
    # Builds a packet to set all LEDs on all clients to the same (arg provided) color

    def SetAllColor(color):
        # Build the packet
        packet =    Globals.COMMAND_ID.to_bytes(2, Globals.ENDIANNESS)  # CommandID (bytes 0,1)
        packet +=   Globals.CHANNEL_ID.to_bytes(2, Globals.ENDIANNESS)  # ChannelID (bytes 2,3)
        packet +=   Globals.LED_COUNT.to_bytes(4, Globals.ENDIANNESS)   # Length (bytes 4 - 7)
        packet +=   int(0).to_bytes(8, Globals.ENDIANNESS)              # Seconds (bytes 8 - 15)
        packet +=   int(0).to_bytes(8, Globals.ENDIANNESS)              # Micros (bytes 16 - 24)
        packet +=   color*Globals.LED_COUNT                             # RGB (bytes 25+)
        
        # Send the build packet to all clients
        for client in Controller.__clients:
            client.send(packet)