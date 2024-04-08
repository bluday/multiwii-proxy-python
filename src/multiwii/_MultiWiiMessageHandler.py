class _MultiWiiMessageHandler(object):
    """
    The class for managing and analyzing MultiWii messages.
    """

    # ------------------------------------ CLASS CONSTANTS -------------------------------------

    """
    The fixed MultiWii preamble used for all messages.
    """
    __MESSAGE_PREAMBLE: str = '$M'

    """
    The incoming direction character for an incoming MultiWii message.
    """
    __MESSAGE_DIRECTION_INCOMING: str = '<'

    """
    The outgoing direction character for an incoming MultiWii message.
    """
    __MESSAGE_DIRECTION_OUTGOING: str = '>'

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_crc(data: bytes) -> int:
        """
        Calculates the a single byte checksum using CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): A serialized payload buffer.

        Returns:
            int: The calculated CRC value for the provided payload.
        """
        checksum = 0

        for byte in data: checksum ^= byte

        return checksum

    # ------------------------------------- CLASS METHODS --------------------------------------

    @classmethod
    def get_message_direction_char(cls, incoming: bool = True) -> str:
        """
        Gets the incoming or outgoing message direction character depending on the provided
        boolean value.

        Parameters:
            incoming (bool): Determines the direction character.

        Returns:
            str: The direction character as a string.
        """
        if incoming:
            return cls.__MESSAGE_DIRECTION_INCOMING

        return cls.__MESSAGE_DIRECTION_OUTGOING

    @classmethod
    def get_message_preamble(cls) -> str:
        """
        Gets the fixed MultiWii preamble string.

        Returns:
            str: Really?
        """
        return cls.__MESSAGE_PREAMBLE
