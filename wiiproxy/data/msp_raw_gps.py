from . import _MspDataStructure, _Point2D, command_code, struct_format

from ..msp_commands import MSP_RAW_GPS

from typing import NamedTuple, NoReturn

@command_code(MSP_RAW_GPS)
@struct_format('2B2I3H')
class MspRawGps(_MspDataStructure):
    """Represents data values for the MSP_RAW_GPS command."""

    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _fix: int

    _satellites: int

    _coordinates: _Point2D[float]

    _altitude: int

    _speed: int

    _ground_course: int

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        """Initializes a new instance with default values."""
        self._fix           = None
        self._satellites    = None
        self._coordinates   = None
        self._altitude      = None
        self._speed         = None
        self._ground_course = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def fix(self) -> int:
        """Gets the fix value."""
        return self._fix

    @property
    def satellites(self) -> int:
        """Gets the satellites value."""
        return self._satellites

    @property
    def coordinates(self) -> _Point2D[float]:
        """Gets the current coordinates."""
        return self._coordinates

    @property
    def altitude(self) -> int:
        """Gets the current altitude."""
        return self._altitude

    @property
    def speed(self) -> int:
        """Gets the current speed."""
        return self._speed

    @property
    def ground_course(self) -> int:
        """Gets the ground course value."""
        return self._ground_course

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _update(self, data: tuple) -> NoReturn:
        """Updates the current values by unserialized data values."""
        self._fix           = data[0]
        self._satellites    = data[1]
        self._coordinates   = data[2] / 10000000
        self._altitude      = data[3] / 10000000
        self._speed         = data[4]
        self._ground_course = data[5] * 10

def MspSetRawGps(NamedTuple):
    """Represents data values for the MSP_SET_RAW_GPS command."""
    fix: int

    satellites: int

    latitude:  int
    longitude: int

    altitude: int

    speed: int

    groundcourse: int
