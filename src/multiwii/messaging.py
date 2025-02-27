from ._command import _MspCommand

from typing import Final, NamedTuple
from struct import pack, unpack

MESSAGE_ERROR_HEADER: Final[bytes] = b'$M!'
"""bytes: The serialized error message header. (0x24, 0x4d, 0x21)"""

MESSAGE_INCOMING_HEADER: Final[bytes] = b'$M<'
"""bytes: The serialized incoming message header. (0x24, 0x4d, 0x3c)"""

MESSAGE_OUTGOING_HEADER: Final[bytes] = b'$M>'
"""bytes: The serialized outgoing message header. (0x24, 0x4d, 0x3e)"""

class _MspResponseMessage(NamedTuple):
    """
    Represents a tuple with the data size and values for a received MSP message.

    Attributes
    ----------
    command : _MspCommand
        An instance of `_MspCommand` of the targeted MSP command.
    data : tuple[int]
        A tuple of parsed data values.
    data_size : int
        The size of the unserialized data values.
    """
    command: _MspCommand

    data: tuple[int]

    data_size: int

class MspMessageError(Exception):
    """Represents a specific errors related to MSP messages."""
    pass

def _crc8_xor(payload: bytes) -> int:
    """
    Calculates the checksum for the payload using an XOR CRC.

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

    for byte in payload: checksum ^= byte

    return checksum & 0xff

def _create_request_message(command: _MspCommand, data: tuple[int]) -> bytes:
    """
    Constructs a serialized message for a provided command and data values.

    Attributes
    ----------
    command : _MspCommand
        An instance of `_MspCommand` representing the MSP command used to create the
        message.
    data : tuple[int]
        The data values to serialize and include in the payload.

    Returns
    -------
    bytes
        The full message in bytes.
    """
    data_size = 0

    payload_content = bytes()

    if data:
        if command.has_variable_size:
            data_size = len(data) / command.data_field_count
        else:
            data_size = command.data_size

        payload_content = pack(command.data_struct_format, *data)

    payload_header = pack('<2B', data_size, command.code)

    payload = payload_header + payload_content

    checksum = pack('<B', _crc8_xor(payload))

    return MESSAGE_OUTGOING_HEADER + payload + checksum

def _decode_names(data: tuple) -> tuple[str]:
    """
    Decodes the deserialized string value and splits it to a tuple.

    Parameters
    ----------
    data : tuple
        The `struct` unpacked payload tuple to decode.

    Returns
    -------
    tuple[str]
        A tuple of decoded names.
    """
    return tuple(data[0].decode('ascii').split(';'))

def _parse_response_message(command: _MspCommand, payload: bytes) -> _MspResponseMessage:
    """
    Parses the payload of a response message for a given command.

    Attributes
    ----------
    command : _MspCommand
        An instance of `_MspCommand` representing the MSP command for the response message.
    payload : bytes
        The received payload buffer from a response message.

    Raises
    ------
    ValueError
        If the command code in the payload does not match the code of the provided
        command.

    Returns
    -------
    _MspResponseMessage
        A named tuple with the command, parsed data and additional information.
    """
    command_code = payload[1]

    if command_code != command.code:
        raise ValueError(
            'Payload with an invalid command code detected. ({}, {})'.format(
                command.code,
                command_code
            )
        )

    data = unpack(command.data_struct_format, payload[2:])

    data_size = payload[0]

    return _MspResponseMessage(command, data, data_size)