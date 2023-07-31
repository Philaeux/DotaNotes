from PySide6.QtCore import QObject

from d2notes.data.database import Player
from d2notes.data.player_state import PlayerState


class ApplicationState(QObject):
    match_id = 0
    server_id = 0
    players = []

    def __init__(self):
        super().__init__()
        self.fresh_players()

    def fresh_players(self):
        self.players = [
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
        ]
