from PySide6.QtCore import QObject

from dota_notes.data.models import PlayerEntity


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
            Set (steam_id -> PlayerState) of players before the cleaning
        """
        old_player_state = {}
        for player in self.players:
            old_player_state[player.steam_id] = player
        self.players = [
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
            PlayerState(), PlayerState(), PlayerState(), PlayerState(), PlayerState(),
        ]
        return old_player_state

    def enrich_with_database(self, session):
        """Fetch the database information about players and update the state with them

        Args:
            session: database session
        """
        for player in self.players:
            if player.steam_id == 0:
                continue
            player_db = session.get(PlayerEntity, str(player.steam_id))
            if player_db is not None:
                PlayerEntity.import_export(player_db, player)

    def enrich_with_old_player_state(self, old_player_state):
        """Enrich with the data from an old state

        Args:
            old_player_state: information about players of another game
        """
        for player in self.players:
            if player.steam_id in old_player_state:
                for at in PlayerState.ATTRIBUTES_TO_COPY:
                    setattr(player, at, getattr(old_player_state[player.steam_id], at))

    def update_with_gsi(self, json):
        """Update with information from the GameStateIntegration (spectate only)

        Args:
            json: GSI information
        """
        if "match_id" in json:
            self.match_id = int(json["match_id"])
        else:
            self.match_id = 0
        self.server_id = 0

        old_player_state = self.fresh_players()
        for index, player in enumerate(json["players"]):
            self.players[index].steam_id = player["accountid"]
            self.players[index].name = player["name"]
        self.enrich_with_old_player_state(old_player_state)

    def update_with_live_game(self, json):
        """Update with information of a live game (Steam Web API)

        Args:
            json: Web API return info
        """
        if "match" in json:
            if "server_steam_id" in json["match"]:
                self.server_id = int(json["match"]["server_steam_id"])
            if "match_id" in json["match"]:
                self.match_id = int(json["match"]["match_id"])

        old_player_state = self.fresh_players()
        if "teams" in json and isinstance(json["teams"], list):
            for team in json["teams"]:
                if "players" in team and isinstance(team["players"], list):
                    for player in team["players"]:
                        if "playerid" in player:
                            if "accountid" in player:
                                self.players[player["playerid"]].steam_id = player["accountid"]
                            if "name" in player:
                                self.players[player["playerid"]].name = player["name"]
        self.enrich_with_old_player_state(old_player_state)

    def update_with_last_game(self, json):
        """Use the OpenDota last game information to populate the state.

        Args:
            json: Data from OpenDota API
        """
        if "match_id" in json:
            self.match_id = int(json["match_id"])
        else:
            self.match_id = 0
        self.server_id = 0

        old_player_state = self.fresh_players()
        if "players" in json and isinstance(json["players"], list):
            for index, player in enumerate(json["players"]):
                if "account_id" in player:
                    if player["account_id"] is None:
                        self.players[index].steam_id = 0
                        self.players[index].name = "< HIDDEN ACCOUNT >"
                    else:
                        self.players[index].steam_id = int(player["account_id"])
                if "personaname" in player:
                    self.players[index].name = player["personaname"]
        self.enrich_with_old_player_state(old_player_state)


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

    ATTRIBUTES_TO_COPY = ["steam_id", "pro_name", "custom_name", "smurf", "is_racist", "is_sexist", "is_toxic",
                          "is_feeder", "gives_up", "destroys_items", "note"]
