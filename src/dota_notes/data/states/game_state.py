from PySide6.QtCore import QObject

from dota_notes.data.messages import MessageGSI
from dota_notes.data.models.player_entity import PlayerEntity
from dota_notes.data.states.player_state import PlayerState


class GameState(QObject):
    """In memory information about a game

    Attributes:
        match_id: unique identifier of a match
        players: list of all the player in the game
    """
    last_gsi_match_id = 0
    match_id = 0
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

    def enrich_players_with_database(self, session):
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

    def enrich_players_with_old_player_state(self, old_player_state):
        """Enrich with the data from an old state

        Args:
            old_player_state: information about players of another game
        """
        for player in self.players:
            if player.steam_id in old_player_state:
                player.copy_from(old_player_state[player.steam_id])

    def update_with_live_game(self, json):
        """Update with information of a live game (Steam Web API)

        Args:
            json: Web API return info
        """
        self.match_id = 0
        old_player_state = self.fresh_players()
        if ("data" not in json
                or "live" not in json["data"]
                or "match" not in json["data"]["live"]):
            return

        match_json = json["data"]["live"]["match"]
        if "matchId" in match_json and match_json["matchId"] is not None:
            self.match_id = match_json["matchId"]
        if "players" not in match_json or not isinstance(match_json["players"], list):
            return

        for index, player in enumerate(match_json["players"]):
            if "steamAccount" in player and player["steamAccount"] is not None:
                account = player["steamAccount"]
                self.players[index].enrich_with_stratz_account_info(account)
        self.enrich_players_with_old_player_state(old_player_state)

    def update_with_last_game(self, json):
        """Use the Stratz last game information to populate the state.

        Args:
            json: Data from OpenDota API
        """
        self.match_id = 0
        old_player_state = self.fresh_players()

        if ("data" not in json
                or "player" not in json["data"]
                or "matches" not in json["data"]["player"]
                or not isinstance(json["data"]["player"]["matches"], list)
                or len(json["data"]["player"]["matches"]) == 0):
            return

        match_json = json["data"]["player"]["matches"][0]
        if "id" in match_json and match_json["id"] is not None:
            self.match_id = match_json["id"]
        if "players" not in match_json or not isinstance(match_json["players"], list):
            return

        for index, player in enumerate(match_json["players"]):
            if "steamAccount" in player and player["steamAccount"] is not None:
                account = player["steamAccount"]
                self.players[index].enrich_with_stratz_account_info(account)
        self.enrich_players_with_old_player_state(old_player_state)

    def enrich_players_with_stratz_info(self, json):
        """Enrich the state by importing player info from a stratz json

        Args
            json: json returned by stratz API
        """
        if "data" not in json:
            return

        for player in self.players:
            if f"p{player.steam_id}" in json["data"]:
                extra_info = json["data"][f"p{player.steam_id}"]

                if "matchCount" in extra_info and extra_info["matchCount"] is not None:
                    player.match_count = extra_info["matchCount"]
                if "steamAccount" in extra_info and extra_info["steamAccount"] is not None:
                    account = extra_info["steamAccount"]
                    player.enrich_with_stratz_account_info(account)
