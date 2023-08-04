from typing import Optional
from enum import Enum


class MessageType(Enum):
    UNKNOWN = 0
    CLIENTS_STATUS = 1
    CLIENTS_CONNECT = 2
    SERVER_ID_REQUEST = 3
    SERVER_ID_RESPONSE = 4


class Message:
    message_type: MessageType = MessageType.UNKNOWN
    payload: Optional[object]

    def __init__(self, message_type: MessageType, payload: Optional[object] = None):
        self.message_type = message_type
        self.payload = payload


class MessageConSatus:
    steam: str
    dota: str

    def __init__(self, steam: str, dota: str):
        self.steam = steam
        self.dota = dota


class MessageServerIdRequest:
    account_id: str

    def __init__(self, account_id: str):
        self.account_id = account_id


class MessageServerIdResponse:
    server_id: int

    def __init__(self, server_id: int):
        self.server_id = server_id
