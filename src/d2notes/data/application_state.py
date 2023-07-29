from PySide6.QtCore import QObject

from d2notes.data.player_state import Player


class ApplicationState(QObject):
    match_id = 0
    server_id = 0
    players = [
        Player(), Player(), Player(), Player(), Player(),
        Player(), Player(), Player(), Player(), Player(),
    ]

    def __init__(self):
        super().__init__()

    def update_with_json(self, json):
        if "match" in json:
            if "server_steam_id" in json["match"]:
                self.server_id = int(json["match"]["server_steam_id"])
            if "match_id" in json["match"]:
                self.match_id = int(json["match"]["match_id"])
        if "teams" in json and isinstance(json["teams"], list):
            for team in json["teams"]:
                if "players" in team and isinstance(team["players"], list):
                    for player in team["players"]:
                        if "playerid" in player:
                            if "accountid" in player:
                                self.players[player["playerid"]].steam_id = player["accountid"]
                            if "name" in player:
                                self.players[player["playerid"]].name = player["name"]
