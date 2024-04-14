from .msp_message_direction import MspMessageDirection

from typing import Final

class MspMessageHeader(object):
    """The class for managing and analyzing MultiWii messages."""

    """The fixed MSP v1 preamble used for all messages."""
    PREAMBLE: Final[str] = '$M'

    """The incoming header."""
    INCOMING: Final[str] = f'{PREAMBLE}{MspMessageDirection.INCOMING}'

    """The outgoing header."""
    OUTGOING: Final[str] = f'{PREAMBLE}{MspMessageDirection.OUTGOING}'

    """ A serialized preamble."""
    SERIALIZED_PREAMBLE: Final[bytes] = int()

    """A serialized incoming header."""
    SERIALIZED_INCOMING: Final[bytes] = int()

    """A serialized outgoing header."""
    SERIALIZED_OUTGOING: Final[bytes] = int()
