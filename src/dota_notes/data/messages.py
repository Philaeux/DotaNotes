class MessageGSI:
    """MatchId send by the GSI"""
    match_id: str

    def __init__(self, match_id):
        self.match_id = match_id
