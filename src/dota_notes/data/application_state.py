from PySide6.QtCore import QObject

from dota_notes.data.player_state import PlayerState


class ApplicationState(QObject):
    match_id = 0
    server_id = 0
    players = []

    def __init__(self):
        super().__init__()
        self.fresh_players()

    def fresh_players(self):
        old_player_state = {}
        for player in self.players:
            old_player_state[player.steam_id] = player
        self.players = [
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
        ]
        return old_player_state
