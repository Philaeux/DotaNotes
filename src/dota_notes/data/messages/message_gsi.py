class MessageGSIPlayer:
    """A player info in the MessageGSI, only available when spectate"""
    steam_id: int
    name: str

    def __init__(self, steam_id, name):
        self.steam_id = steam_id
        self.name = name


class MessageGSI:
    """MatchId send by the GSI, with players id if spectating"""
    match_id: str
    players: list[MessageGSIPlayer]

    def __init__(self, match_id):
        self.match_id = match_id
        self.players = []
