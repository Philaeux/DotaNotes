import sys
from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session
from d2notes.data.database import Setting, Player
from d2notes.helpers import get_game_live_stats
from d2notes.ui.main_window import MainWindow


class QtApp:
    def __init__(self, d2notes):
        self.d2notes = d2notes

        # Build App
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.lastIndexSelected = 0

        # Connect actions
        self.window.actionSettings.triggered.connect(lambda: print("TODO"))
        self.window.actionExit.triggered.connect(self.window.close)
        self.window.buttonBububu.clicked.connect(lambda: self.window.inputSteamId.setText("76561198066647717"))
        self.window.buttonBulldog.clicked.connect(lambda: self.window.inputSteamId.setText("76561198053098358"))
        self.window.buttonGrubby.clicked.connect(lambda: self.window.inputSteamId.setText("76561198809738927"))
        self.window.buttonPhilaeux.clicked.connect(lambda: self.window.inputSteamId.setText("76561197961298382"))
        self.window.buttonS4.clicked.connect(lambda: self.window.inputSteamId.setText("76561198001497299"))
        self.window.buttonSearch.clicked.connect(self.on_search_game)
        self.window.buttonDetailsSave.clicked.connect(self.save_player_details)
        for i in range(10):
            getattr(self.window, f"labelPlayer{i}Name").clicked.connect(self.on_label_click)

        with Session(self.d2notes.database.engine) as session:
            last_search = session.get(Setting, "last_search")
            if last_search is not None:
                self.window.inputSteamId.setText(last_search.value)

        self.status_message("Ready")

        self.window.show()

    def status_message(self, message, timeout=0):
        self.window.statusBar().showMessage(datetime.now().strftime("%H:%M:%S - ") + message, timeout)

    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.process_queues)
        timer.start(100)

        return_code = self.app.exec_()
        return return_code

    def process_queues(self):
        while not self.d2notes.match_information_from_gsi.empty():
            match_info = self.d2notes.match_information_from_gsi.get(block=False)
            if self.d2notes.state.match_id != match_info["match_id"]:
                self.d2notes.state.match_id = match_info["match_id"]
                self.d2notes.state.server_id = 0
                self.status_message(f"Detected match {self.d2notes.state.match_id!s} from GSI.")
                self.update_state_with_gsi(self.d2notes.state, match_info)
                self.draw_match_with_state(self.d2notes.state)
                self.draw_details_with_player(0)
        while not self.d2notes.server_id_from_dota.empty():
            server_id = self.d2notes.server_id_from_dota.get(block=False)
            if server_id != 0:
                self.d2notes.state.server_id = server_id
                game_json = get_game_live_stats(self.d2notes.steam_api_key, self.d2notes.state.server_id)
                self.update_state_with_json(self.d2notes.state, game_json)
                self.update_state_with_database(self.d2notes.state)
                self.status_message("Found game info for player " + self.window.inputSteamId.text() + " using WEBAPI.")
                self.draw_match_with_state(self.d2notes.state)
                self.draw_details_with_player(0)
            else:
                self.status_message("No game found for player " + self.window.inputSteamId.text())

    def on_open_settings(self):
        pass

    def on_label_click(self, label_name, label_text):
        row = 0
        for char in label_name:
            if char.isdigit():
                row = int(char)
        self.draw_details_with_player(row)

    def draw_details_with_player(self, player_slot):
        self.lastIndexSelected = player_slot

        player_state = self.d2notes.state.players[player_slot]
        self.window.labelDetailsSteamId.setText(str(player_state.steam_id))
        self.window.labelDetailsName.setText(player_state.name)
        self.window.labelDetailsProName.setText(
            player_state.pro_name if player_state.pro_name is not None else "")
        self.window.inputDetailsCustomName.setText(player_state.custom_name)
        self.window.comboBoxDetailsSmurf.setCurrentText(player_state.smurf)
        self.window.checkBoxDetailsRacist.setChecked(player_state.is_racist)
        self.window.checkBoxDetailsSexist.setChecked(player_state.is_sexist)
        self.window.checkBoxDetailsToxic.setChecked(player_state.is_toxic)
        self.window.checkBoxDetailsFeeder.setChecked(player_state.is_feeder)
        self.window.checkBoxDetailsGivesUp.setChecked(player_state.gives_up)
        self.window.checkBoxDetailsDestroysItems.setChecked(player_state.destroys_items)
        self.window.inputDetailsNote.setPlainText(player_state.note)

    def draw_match_with_state(self, data):
        self.window.labelMatchId.setText(str(data.match_id))
        self.window.labelServerId.setText(str(data.server_id))
        for index, player in enumerate(data.players):
            if index > 9:
                break
            self.draw_match_player(index, player)

    def draw_match_player(self, player_slot, player_data):
        getattr(self.window, f"labelPlayer{player_slot}Name").setText(player_data.name)
        getattr(self.window, f"labelPlayer{player_slot}ProName").setText(
            player_data.pro_name if player_data.pro_name is not None else "")
        getattr(self.window, f"labelPlayer{player_slot}CustomName").setText(
            player_data.custom_name if player_data.custom_name is not None else "")
        getattr(self.window, f"labelPlayer{player_slot}Smurf").setText(player_data.smurf)
        getattr(self.window, f"labelPlayer{player_slot}FlagRacist").setVisible(player_data.is_racist)
        getattr(self.window, f"labelPlayer{player_slot}FlagSexist").setVisible(player_data.is_sexist)
        getattr(self.window, f"labelPlayer{player_slot}FlagToxic").setVisible(player_data.is_toxic)
        getattr(self.window, f"labelPlayer{player_slot}FlagFeeder").setVisible(player_data.is_feeder)
        getattr(self.window, f"labelPlayer{player_slot}FlagGivesUp").setVisible(player_data.gives_up)
        getattr(self.window, f"labelPlayer{player_slot}FlagDestroyer").setVisible(player_data.destroys_items)

    def on_search_game(self):
        if self.window.inputSteamId.text() != "":
            self.d2notes.user_steam_id_to_dota.put(self.window.inputSteamId.text())
            with Session(self.d2notes.database.engine) as session:
                last_search = session.query(Setting).filter_by(key="last_search").one_or_none()
                if last_search is not None:
                    last_search.value = self.window.inputSteamId.text()
                else:
                    last_search = Setting("last_search", self.window.inputSteamId.text())
                    session.add(last_search)
                session.commit()

    def update_state_with_json(self, state, json):
        if "match" in json:
            if "server_steam_id" in json["match"]:
                state.server_id = int(json["match"]["server_steam_id"])
            if "match_id" in json["match"]:
                state.match_id = int(json["match"]["match_id"])
        if "teams" in json and isinstance(json["teams"], list):
            old_player_state = state.fresh_players()
            for team in json["teams"]:
                if "players" in team and isinstance(team["players"], list):
                    for player in team["players"]:
                        if "playerid" in player:
                            if "accountid" in player:
                                state.players[player["playerid"]].steam_id = player["accountid"]
                                if player["accountid"] in old_player_state:
                                    state.players[player["playerid"]].__dict__ = old_player_state[player["accountid"]].__dict__.copy()
                            if "name" in player:
                                state.players[player["playerid"]].name = player["name"]

    def update_state_with_gsi(self, state, match_info):
        old_player_state = state.fresh_players()
        for index, player in enumerate(match_info["players"]):
            state.players[index].steam_id = player["accountid"]
            if player["accountid"] in old_player_state:
                state.players[index].__dict__ = old_player_state[player["accountid"]].__dict__.copy()
            state.players[index].name = player["name"]

    def update_state_with_database(self, state):
        with Session(self.d2notes.database.engine) as session:
            for player in state.players:
                if player.steam_id == 0:
                    continue
                player_db = session.get(Player, str(player.steam_id))
                if player_db is not None:
                    Player.import_export(player_db, player)

    def save_player_details(self):
        player_state = self.d2notes.state.players[self.lastIndexSelected]
        player_state.pro_name = \
            self.window.labelDetailsProName.text() if self.window.labelDetailsProName != "" else None
        player_state.custom_name = self.window.inputDetailsCustomName.text()
        player_state.smurf = self.window.comboBoxDetailsSmurf.currentText()
        player_state.is_racist = self.window.checkBoxDetailsRacist.isChecked()
        player_state.is_sexist = self.window.checkBoxDetailsSexist.isChecked()
        player_state.is_toxic = self.window.checkBoxDetailsToxic.isChecked()
        player_state.is_feeder = self.window.checkBoxDetailsFeeder.isChecked()
        player_state.gives_up = self.window.checkBoxDetailsGivesUp.isChecked()
        player_state.destroys_items = self.window.checkBoxDetailsDestroysItems.isChecked()
        player_state.note = self.window.inputDetailsNote.toPlainText()
        self.draw_match_player(self.lastIndexSelected, player_state)
        with Session(self.d2notes.database.engine) as session:
            player_info = session.get(Player, str(player_state.steam_id))
            if player_info is None:
                player_info = Player.make_from_state(player_state)
                session.add(player_info)
            else:
                player_info.name = player_state.name
                Player.import_export(player_state, player_info)
            session.commit()
