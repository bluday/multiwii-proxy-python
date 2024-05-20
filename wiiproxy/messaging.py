from typing import Final

# --------------------------------------- CONSTANTS ----------------------------------------

ERROR_HEADER:    Final[bytes] = b'$M!' # 0x24, 0x4d, 0x21

INCOMING_HEADER: Final[bytes] = b'$M<' # 0x24, 0x4d, 0x3c

OUTGOING_HEADER: Final[bytes] = b'$M>' # 0x24, 0x4d, 0x3e

# --------------------------------------- FUNCTIONS ----------------------------------------

def decode_names(data: tuple) -> tuple[str]:
    """Decodes the deserialized string value and splits it to a tuple.

    Parameters
    ----------
    data : tuple
        The `struct` unpacked payload tuple to decode.

    Raises
    ------
    TypeError
        If `data` is not of type `tuple`.
    UnicodeDecodeError
        If the bytes cannot be decoded into ASCII characters.

    Returns
    -------
    tuple[str]
        A tuple of decoded names.
    """
    return tuple(data[0].decode('ascii').split(';'))

def calculate_checksum(payload: bytes) -> int:
    """Calculates the checksum for the payload using an XOR CRC.

    Parameters
    ----------
    payload : bytes
        Bytes of the full payload (including the command code and size).

    Returns
    -------
    int
        The checksum for the provided payload.
    """
    checksum = 0

    for byte in data: checksum ^= byte

    return checksum & 0xff
