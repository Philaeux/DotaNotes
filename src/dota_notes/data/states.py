from PySide6.QtCore import QObject


class GameState(QObject):
    """In memory information about a game

    Attributes:
        match_id: unique identifier of a match
        server_id: unique identifier of the server the match is played on
        players: list of all the player in the game
    """
    match_id = 0
    server_id = 0
    players = []

    def __init__(self):
        super().__init__()
        self.fresh_players()

    def fresh_players(self):
        """Clean the list of players.

        Returns
            list of players before the cleaning
        """
        old_player_state = {}
        for player in self.players:
            old_player_state[player.steam_id] = player
        self.players = [
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
        ]
        return old_player_state


class PlayerState(QObject):
    """In memory information about a player. Attributes similar to the PlayerEntity"""
    steam_id = 0
    name = ""
    pro_name = None
    custom_name = ""
    smurf = ""
    is_racist = False
    is_sexist = False
    is_toxic = False
    is_feeder = False
    gives_up = False
    destroys_items = False
    note = ""
