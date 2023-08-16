class MessageServerIdRequest:
    """Request the server ID a specific account is playing on"""
    steam_id: int

    def __init__(self, steam_id: int):
        self.steam_id = steam_id


class MessageServerIdResponse:
    """Server ID where a specific player is playing on"""
    server_id: int

    def __init__(self, server_id: int):
        self.server_id = server_id
