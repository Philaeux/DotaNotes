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
        