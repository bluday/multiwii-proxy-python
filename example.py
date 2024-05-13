#! /usr/bin/env python3

from wiiproxy.msp_message import MspMessage
from wiiproxy.msp_data    import MspIdent, MspRawImu

print(f'Header preamble: {MspMessage.HEADER_PREAMBLE}')
print(f'Incoming header: {MspMessage.INCOMING_HEADER}')
print(f'Outgoing header: {MspMessage.OUTGOING_HEADER}')
