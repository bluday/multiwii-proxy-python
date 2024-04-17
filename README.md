# wiiproxy

_Not functional at this time. The codebase is currently being revamped and improved._

WiiProxy is a user-friendly and multithreaded Python 3 module for controlling _MultiWii_-based drones.

Supports only v1 of the [MultiWi Serial Protocol (MSP)](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol)—and not v2 or any of the newer versions.

### Usage:

```python
from serial   import Serial
from wiiproxy import MultiWii

serial = Serial('/dev/ttyUSB0', baudrate=115200)

fc = MultiWii(serial)

fc.start()

print(f'{fc.indent.multitype}') # QuadX
```
