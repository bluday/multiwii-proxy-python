from typing import Final

class _MultiWiiMessageHandler(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    # ------------------------------------ CLASS VARIABLES -------------------------------------

    """
    The fixed MultiWii preamble used for all messages.
    """
    MESSAGE_PREAMBLE: Final[str] = '$M'

    """
    The incoming direction character.
    """
    MESSAGE_INCOMING_CHAR: Final[str] = '<'

    """
    The outgoing direction character.
    """
    MESSAGE_OUTGOING_CHAR: Final[str] = '>'

    """
    The error direction character.
    """
    MESSAGE_ERROR_CHAR: Final[str] = '!'

    """
    The preamble in bytes.
    """
    MESSAGE_SERIALIZED_PREAMBLE: Final[bytes] = MESSAGE_PREAMBLE.encode('ascii')
    
    """
    The incoming direction character as a byte.
    """
    MESSAGE_SERIALIZED_INCOMING_CHAR: Final[int] = ord(MESSAGE_INCOMING_CHAR) & 0xff

    """
    The outgoing direction character as a byte.
    """
    MESSAGE_SERIALIZED_OUTGOING_CHAR: Final[int] = ord(MESSAGE_OUTGOING_CHAR) & 0xff

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_crc(payload: bytes) -> int:
        """
        Calculates the a single byte checksum using CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): A serialized payload buffer.

        Returns:
            int: The calculated CRC value for the provided payload.
        """
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum
