import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session

from dota_notes.data.models import SettingEntity, PlayerEntity
from dota_notes.data.messages import MessageServerIdResponse, MessageConnectionStatus, MessageServerIdRequest, \
    MessageConnect
from dota_notes.helpers import get_game_live_stats
from dota_notes.ui.main_window import MainWindow


class QtApp:
    """Qt application process"""

    def __init__(self, dota_notes):
        self.dota_notes = dota_notes

        # Build Qt app components
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.lastIndexSelected = 0

        # Connect actions
        self.window.actionSettings.triggered.connect(self.on_open_settings)
        self.window.actionExit.triggered.connect(self.window.close)
        self.window.buttonSettingsSave.clicked.connect(self.on_settings_save)
        self.window.buttonSettingsCancel.clicked.connect(self.on_settings_cancel)
        self.window.buttonConnect.clicked.connect(self.on_connect_client)
        self.window.buttonBububu.clicked.connect(lambda: self.window.inputSteamId.setText("76561198066647717"))
        self.window.buttonBulldog.clicked.connect(lambda: self.window.inputSteamId.setText("76561198053098358"))
        self.window.buttonGrubby.clicked.connect(lambda: self.window.inputSteamId.setText("76561198809738927"))
        self.window.buttonPhilaeux.clicked.connect(lambda: self.window.inputSteamId.setText("76561197961298382"))
        self.window.buttonS4.clicked.connect(lambda: self.window.inputSteamId.setText("76561198001497299"))
        self.window.buttonSearch.clicked.connect(self.on_search_game)
        self.window.buttonDetailsSave.clicked.connect(self.on_save_player_details)
        for i in range(10):
            getattr(self.window, f"labelPlayer{i}Name").clicked.connect(self.on_label_click)

        with Session(self.dota_notes.database.engine) as session:
            last_search = session.get(SettingEntity, "last_search")
            if last_search is not None:
                self.window.inputSteamId.setText(last_search.value)
        self.window.show()

    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.process_queues)
        timer.start(100)

        return_code = self.app.exec_()
        return return_code

    def process_queues(self):
        while not self.dota_notes.match_information_from_gsi.empty():
            match_info = self.dota_notes.match_information_from_gsi.get(block=False)
            if self.dota_notes.state.match_id != match_info["match_id"] and self.dota_notes.settings.gsi_spectate:
                self.dota_notes.state.match_id = match_info["match_id"]
                self.dota_notes.state.server_id = 0
                self.window.draw_status_message(f"Detected match {self.dota_notes.state.match_id!s} from GSI.")
                self.update_state_with_gsi(self.dota_notes.state, match_info)
                self.window.draw_match_with_state(self.dota_notes.state)
                self.draw_details_with_player(0)
        while not self.dota_notes.message_queue_qt.empty():
            message = self.dota_notes.message_queue_qt.get(block=False)
            if isinstance(message, MessageServerIdResponse):
                if message.server_id != 0:
                    self.dota_notes.state.server_id = message.server_id
                    game_json = get_game_live_stats(self.dota_notes.settings.steam_api_key, self.dota_notes.state.server_id)
                    self.update_state_with_json(self.dota_notes.state, game_json)
                    self.update_state_with_database(self.dota_notes.state)
                    self.window.draw_status_message("Found game info for player " + self.window.inputSteamId.text() + " using WEBAPI.")
                    self.window.draw_match_with_state(self.dota_notes.state)
                    self.draw_details_with_player(0)
                else:
                    self.window.draw_status_message("No game found for player " + self.window.inputSteamId.text())
            elif isinstance(message, MessageConnectionStatus):
                self.window.draw_connection_status(message.steam, message.dota)

    def on_open_settings(self):
        settings = self.dota_notes.settings
        self.window.comboBoxSettingsMode.setCurrentText(settings.software_mode)
        self.window.checkBoxGSI.setChecked(settings.gsi_spectate)
        self.window.lineEditSettingsProxyURL.setText(settings.proxy_url)
        self.window.lineEditSettingsProxyAPIKey.setText(settings.proxy_api_key)
        self.window.lineEditSettingsSteamUser.setText(settings.steam_user)
        self.window.lineEditSettingsSteamPassword.setText(settings.steam_password)
        self.window.lineEditSettingsSteamAPIKey.setText(settings.steam_api_key)
        self.window.centralStackedWidget.setCurrentIndex(1)

    def on_settings_save(self):
        settings = self.dota_notes.settings
        settings.software_mode = self.window.comboBoxSettingsMode.currentText()
        settings.gsi_spectate = self.window.checkBoxGSI.isChecked()
        settings.proxy_url = self.window.lineEditSettingsProxyURL.text()
        settings.proxy_api_key = self.window.lineEditSettingsProxyAPIKey.text()
        settings.steam_user = self.window.lineEditSettingsSteamUser.text()
        settings.steam_password = self.window.lineEditSettingsSteamPassword.text()
        settings.steam_api_key = self.window.lineEditSettingsSteamAPIKey.text()
        with Session(self.dota_notes.database.engine) as session:
            settings.export_to_database(session)
        self.window.centralStackedWidget.setCurrentIndex(0)

    def on_settings_cancel(self):
        self.window.centralStackedWidget.setCurrentIndex(0)

    def on_connect_client(self):
        self.window.buttonConnect.setVisible(False)
        message = MessageConnect(self.dota_notes.settings.steam_user, self.dota_notes.settings.steam_password)
        self.dota_notes.message_queue_dota.put(message)

    def on_label_click(self, label_name, label_text):
        row = 0
        for char in label_name:
            if char.isdigit():
                row = int(char)
        self.draw_details_with_player(row)

    def draw_details_with_player(self, player_slot):
        self.lastIndexSelected = player_slot

        player_state = self.dota_notes.state.players[player_slot]
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

    def on_search_game(self):
        if self.window.inputSteamId.text() != "":
            self.dota_notes.message_queue_dota.put(MessageServerIdRequest(self.window.inputSteamId.text()))
            with Session(self.dota_notes.database.engine) as session:
                last_search = session.query(SettingEntity).filter_by(key="last_search").one_or_none()
                if last_search is not None:
                    last_search.value = self.window.inputSteamId.text()
                else:
                    last_search = SettingEntity("last_search", self.window.inputSteamId.text())
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
        with Session(self.dota_notes.database.engine) as session:
            for player in state.players:
                if player.steam_id == 0:
                    continue
                player_db = session.get(PlayerEntity, str(player.steam_id))
                if player_db is not None:
                    PlayerEntity.import_export(player_db, player)

    def on_save_player_details(self):
        player_state = self.dota_notes.state.players[self.lastIndexSelected]
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
        self.window.draw_match_player(self.lastIndexSelected, player_state)
        with Session(self.dota_notes.database.engine) as session:
            player_info = session.get(PlayerEntity, str(player_state.steam_id))
            if player_info is None:
                player_info = PlayerEntity.make_from_state(player_state)
                session.add(player_info)
            else:
                player_info.name = player_state.name
                PlayerEntity.import_export(player_state, player_info)
            session.commit()
