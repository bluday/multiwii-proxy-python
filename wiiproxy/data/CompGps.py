from wiiproxy.data.base import MultiWiiDataStructure

from dataclasses import dataclass
from typing      import Final

@dataclass(slots=True)
class CompGps(MultiWiiDataStructure):
    """Represents data values for the MSP_COMP_GPS command."""
    distance_to_home: Final[int] = 0

    direction_to_home: Final[int] = 0

    update: Final[int] = 0 # What?
