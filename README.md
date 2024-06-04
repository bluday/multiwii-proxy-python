
# WiiProxy

## Overview

A simple and user-friendly Python 3 module for controlling _MultiWii_-based drones using version 1.0 of the _MultiWii Serial Protocol (MSP)_.

This module does not support version 2.0, or any of the newer versions, of MSP.

## Documentation

The API documentation can be found on the [documentation site](https://bluday.github.io/wiiproxy/).

## Installation

Run either one of these commands to install the package:

```sh
python setup.py

pip install .
```

## Usage

```python
from serial   import Serial
from wiiproxy import MultiWii

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

ident = multiwii.get_ident()

print(repr(ident.multitype)) # <MultiWiiMultitype.QuadX: 3>
```

Other example usages can be found in the `examples` directory.

## Licensing

This project is licensed under the MIT license. See [LICENSE](https://github.com/BluDay/wiiproxy/blob/master/LICENSE) for more details.
