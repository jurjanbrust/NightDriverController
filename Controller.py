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

import socket, time, Globals

class Controller:
    #FIXME This isn't a very responsible way to manage these clients' lifecycles
    __clients = []
    for client in Globals.CLIENTS:
        __clients.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        __clients[-1].connect((client, 49152))

    # __GetBasePacket
    #
    # Builds the base packet header needed for all messages sent to NightDriverStrip
    #
    # No color data is included in the base packet. That data will need to be
    # appended to the end of the packet before being sent to NightDriverStrip

    def __GetBasePacket(length = Globals.LED_COUNT):
        # Build the packet
        packet =    Globals.COMMAND_ID.to_bytes(2, Globals.ENDIANNESS)  # CommandID (bytes 0,1)
        packet +=   Globals.CHANNEL_ID.to_bytes(2, Globals.ENDIANNESS)  # ChannelID (bytes 2,3)
        packet +=   length.to_bytes(4, Globals.ENDIANNESS)              # Length (bytes 4 - 7)
        packet +=   int(0).to_bytes(8, Globals.ENDIANNESS)              # Seconds (bytes 8 - 15)
        packet +=   int(0).to_bytes(8, Globals.ENDIANNESS)              # Micros (bytes 16 - 24)
        return packet

    # __SendAllClients
    # 
    # Sends the (arg provided) packet to all of the connected clients

    def __SendAllClients(packet):
        for client in Controller.__clients:
            client.send(packet)

    # __IntToBytes
    #
    # Converts an individual Integer value into its equivalent Byte value

    def __IntToBytes(value):
        return int(value).to_bytes(1, Globals.ENDIANNESS)

    # __Wheel
    #
    # Cycle 3 Byte values based on the (arg provided) Wheel Position
    #
    # This function is based on the Wheel function from the Adafruit NeoPixel 
    # library

    def __Wheel(WheelPos):
        WheelPos = 255 - WheelPos

        if WheelPos < 85:
            return Controller.__IntToBytes(255 - WheelPos * 3) + Controller.__IntToBytes(0) + Controller.__IntToBytes(WheelPos * 3)
        if WheelPos < 170:
            WheelPos -= 85
            return Controller.__IntToBytes(0) + Controller.__IntToBytes(WheelPos * 3) + Controller.__IntToBytes(255 - WheelPos * 3)
        WheelPos -= 170
        return Controller.__IntToBytes(WheelPos * 3) + Controller.__IntToBytes(255 - WheelPos * 3) + Controller.__IntToBytes(0)

    # SetAllColor
    #
    # Builds a packet to set all LEDs on all clients to the same (arg provided) color

    def SetAllColor(color):
        packet = Controller.__GetBasePacket()
        packet +=   color*Globals.LED_COUNT
        
        # Send the build packet to all clients
        Controller.__SendAllClients(packet)

    # AllColorCycle
    #
    # Builds a packet to set all LEDs on all clients to the same generated color
    # It will cycle through the colors to create a rainbow effect
    #
    # This function is based on the rainbow function from the Adafruit NeoPixel
    # library

    def AllColorCycle(wait):
        for j in range(256):
            packet = Controller.__GetBasePacket()
            for i in range(Globals.LED_COUNT):
                packet += Controller.__Wheel((i + j) & 255)
            
            Controller.__SendAllClients(packet)
            time.sleep(wait)

    # ColorCycle
    #
    # Builds a packet to set all LEDs on all clients to a (mostly) unique color
    # It will cycle through the colors to create a rainbow effect
    #
    # This function is based on the rainbowCycle function from the Adafruit NeoPixel
    # library

    def ColorCycle(wait):
        for j in range(256 * 3):
            packet = Controller.__GetBasePacket()
            for i in range(Globals.LED_COUNT):
                packet += Controller.__Wheel(int((i * 256 / Globals.LED_COUNT) + j) & 255)

            Controller.__SendAllClients(packet)
            time.sleep(wait)