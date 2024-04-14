from typing import Final

class MspMessageDirection(object):
    """An enum-like class for message direction characters."""

    """The error character."""
    ERROR: Final[str] = '!'
    
    """The incoming direction character."""
    INCOMING: Final[str] = '<'

    """The outgoing direction character."""
    OUTGOING: Final[str] = '>'
    
    """A serialized error character."""
    SERIALIZED_ERROR: Final[int] = int()

    """A serialized incoming direction character."""
    SERIALIZED_INCOMING: Final[int] = int()

    """A serialized outgoing direction character."""
    SERIALIZED_OUTGOING: Final[int] = int()
