class MessageConnect:
    """Ask the client to connect with specific credentials

    Attributes:
        user: steam username
        password: steam password
    """
    user: str
    password: str

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password


class MessageConnectionStatus:
    """Report the status of the connections of steam/dota clients

    Attributes:
        steam: Steam connection status
        dota: Dota connection status
    """
    steam: str
    dota: str

    def __init__(self, steam: str, dota: str):
        self.steam = steam
        self.dota = dota


class MessageServerIdRequest:
    """Request the server ID a specific account is playing on"""
    account_id: str

    def __init__(self, account_id: str):
        self.account_id = account_id


class MessageServerIdResponse:
    """Server ID where a specific player is playing on"""
    server_id: int

    def __init__(self, server_id: int):
        self.server_id = server_id
