# NightDriverController

This project works with clients running Dave Plummer's [NightDriverStrip](https://github.com/PlummersSoftwareLLC/NightDriverStrip). To send color data over the network:
- Ensure ENABLE_WIFI and INCOMING_WIFI_ENABLED are enabled in the client's globals.h
- Connect to the Serial Console (or use some other method) to determine the client's IP address
- Add the client's IP address to Globals.py in this project
- Repeat for as many clients as you would like to add
- Add the number of LEDs attached to the client(s) in Globals.py in this project (currently all clients must use the same number of LEDs)
- Run Main.py using Python version >= 3 (e.g. ```python Main.py``` or ```python3 Main.py```)
