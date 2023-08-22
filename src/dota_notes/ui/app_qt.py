import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session
from steam.steamid import SteamID

from dota_notes.data.messages.message_connect import MessageConnect, MessageDisconnect
from dota_notes.data.messages.message_connection_status import MessageConnectionStatus
from dota_notes.data.messages.message_server_id import MessageServerIdRequest, MessageServerIdResponse
from dota_notes.data.models.settings_entity import SettingEntity
from dota_notes.data.models.player_entity import PlayerEntity
from dota_notes.data.messages.message_gsi import MessageGSI
from dota_notes.helpers import stratz_get_players_info, stratz_get_last_game, stratz_get_live_game, \
    get_steam_live_game_stats
from dota_notes.ui.main_window import MainWindow


class QtApp:
    """Qt application process

    Attributes
        dota_notes: link to the main object of the application
        app: QT app
        window: QT Main window of the application
        last_selected_index: index of the last selected player
        last_selected_player: data of the last selected player
    """

    def __init__(self, dota_notes):
        self.dota_notes = dota_notes

        # Build Qt app components
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.last_selected_index = 0
        self.last_selected_player = None

        # Connect actions
        self.window.actionSettings.triggered.connect(self.on_open_settings)
        self.window.actionExit.triggered.connect(self.window.close)
        self.window.buttonSettingsSave.clicked.connect(self.on_settings_save)
        self.window.buttonSettingsCancel.clicked.connect(self.on_settings_cancel)
        self.window.buttonConnect.clicked.connect(self.on_connect_client)
        self.window.buttonDisconnect.clicked.connect(self.on_disconnect_client)
        self.window.buttonBububu.clicked.connect(lambda: self.window.inputSteamId.setText("106381989"))
        self.window.buttonBulldog.clicked.connect(lambda: self.window.inputSteamId.setText("92832630"))
        self.window.buttonGrubby.clicked.connect(lambda: self.window.inputSteamId.setText("849473199"))
        self.window.buttonPhilaeux.clicked.connect(lambda: self.window.inputSteamId.setText("1032654"))
        self.window.buttonS4.clicked.connect(lambda: self.window.inputSteamId.setText("41231571"))
        self.window.buttonSteamLive.clicked.connect(self.on_steam_live)
        self.window.buttonStratzLive.clicked.connect(self.on_stratz_live)
        self.window.buttonStratzLast.clicked.connect(self.on_stratz_last)
        self.window.buttonStratzInfo.clicked.connect(self.on_stratz_info)
        self.window.buttonDetailsSave.clicked.connect(self.on_save_player_details)
        for i in range(10):
            getattr(self.window, f"labelPlayer{i}Name").clicked.connect(self.on_label_click)
            getattr(self.window, f"labelPlayer{i}CustomName").clicked.connect(self.on_label_click)
            getattr(self.window, f"labelPlayer{i}ProName").clicked.connect(self.on_label_click)
            getattr(self.window, f"labelPlayer{i}GameCount").clicked.connect(self.on_label_click)
            getattr(self.window, f"labelPlayer{i}Smurf").clicked.connect(self.on_label_click)

        with Session(self.dota_notes.database.engine) as session:
            last_search = session.get(SettingEntity, "last_search")
            if last_search is not None:
                self.window.inputSteamId.setText(last_search.value)
        self.window.show()

    def run(self):
        """Start the QT application, enter the event loop and add a periodic dequeue of messages"""
        timer = QTimer()
        timer.timeout.connect(self.process_queues)
        timer.start(100)

        return_code = self.app.exec_()
        return return_code

    def process_queues(self):
        """Periodic process that checks message queues and process necessary jobs"""
        while not self.dota_notes.message_queue_qt.empty():
            message = self.dota_notes.message_queue_qt.get(block=False)
            if isinstance(message, MessageGSI):
                self.dota_notes.state.update_with_gsi(message)
                self.window.draw_match_with_state(self.dota_notes.state)
                self.window.draw_status_message("New match detected on GSI.")
            elif isinstance(message, MessageConnectionStatus):
                self.window.draw_connection_status(message.steam, message.dota)
            elif isinstance(message, MessageServerIdResponse):
                if message.server_id != 0:
                    self.dota_notes.state.server_id = message.server_id
                    json = get_steam_live_game_stats(self.dota_notes.settings.steam_api_key, self.dota_notes.state.server_id)
                    self.dota_notes.state.update_with_steam_live_game(json)
                    with Session(self.dota_notes.database.engine) as session:
                        self.dota_notes.state.enrich_players_with_database(session)
                    self.window.draw_status_message(f"Found game info for player {self.window.inputSteamId.text()} using WEBAPI.")
                    self.window.draw_match_with_state(self.dota_notes.state)
                    self.on_select_player(0)
                else:
                    self.window.draw_status_message("No game found for player " + self.window.inputSteamId.text())

    def on_open_settings(self):
        """User opens the settings panel"""
        settings = self.dota_notes.settings
        self.window.comboBoxSettingsMode.setCurrentText(settings.software_mode)
        self.window.lineEditStratzToken.setText(settings.stratz_token)
        self.window.lineEditSettingsSteamUser.setText(settings.steam_user)
        self.window.lineEditSettingsSteamPassword.setText(settings.steam_password)
        self.window.lineEditSettingsSteamAPIKey.setText(settings.steam_api_key)
        self.window.centralStackedWidget.setCurrentIndex(1)

    def on_settings_save(self):
        """User saves settings modifications"""
        settings = self.dota_notes.settings
        settings.software_mode = self.window.comboBoxSettingsMode.currentText()
        settings.stratz_token = self.window.lineEditStratzToken.text()
        settings.steam_user = self.window.lineEditSettingsSteamUser.text()
        settings.steam_password = self.window.lineEditSettingsSteamPassword.text()
        settings.steam_api_key = self.window.lineEditSettingsSteamAPIKey.text()
        with Session(self.dota_notes.database.engine) as session:
            settings.export_to_database(session)
            session.commit()
        self.window.centralStackedWidget.setCurrentIndex(0)

    def on_settings_cancel(self):
        """User cancels settings modifications"""
        self.window.centralStackedWidget.setCurrentIndex(0)

    def on_connect_client(self):
        """User clicks on connect button"""
        self.window.buttonConnect.setVisible(False)
        message = MessageConnect(self.dota_notes.settings.steam_user, self.dota_notes.settings.steam_password)
        self.dota_notes.message_queue_dota.put(message)

    def on_disconnect_client(self):
        """User clicks on disconnect button"""
        message = MessageDisconnect()
        self.dota_notes.message_queue_dota.put(message)

    def on_label_click(self, label_name, label_text):
        """User clicks on a specific label"""
        row = 0
        for char in label_name:
            if char.isdigit():
                row = int(char)
        self.on_select_player(row)

    def on_select_player(self, player_slot):
        """User select a player to have info off"""
        self.last_selected_index = player_slot
        self.last_selected_player = self.dota_notes.state.players[player_slot]
        self.window.draw_details_with_player(self.last_selected_player)

    def on_steam_live(self):
        """Look for a live game a player is in"""
        steam_id = self.window.inputSteamId.text()
        if self.is_valid_search(steam_id):
            steam_id = SteamID(steam_id)
            self.dota_notes.message_queue_dota.put(MessageServerIdRequest(steam_id.as_64))

    def on_stratz_live(self):
        """Get current game info for a player (if any)"""
        if self.dota_notes.state.match_id == 0:
            return
        json = stratz_get_live_game(self.dota_notes.settings.stratz_token, self.dota_notes.state.match_id)
        if json is not None:
            self.dota_notes.state.update_with_stratz_live_game(json)
            with Session(self.dota_notes.database.engine) as session:
                self.dota_notes.state.enrich_players_with_database(session)
            self.window.draw_match_with_state(self.dota_notes.state)
            self.on_select_player(0)
            self.window.draw_status_message("Found live game in Stratz live data and updated UI.")
        else:
            self.window.draw_status_message(f"No live game info found for match ID {self.dota_notes.state.match_id}.")

    def on_stratz_last(self):
        """Get last game info for a player (if public)"""
        if self.dota_notes.settings.stratz_token == "":
            return
        steam_id = self.window.inputSteamId.text()
        if self.is_valid_search(steam_id):
            steam_id = SteamID(steam_id)
            json = stratz_get_last_game(self.dota_notes.settings.stratz_token, steam_id.as_32)
            if json is not None:
                self.dota_notes.state.update_with_stratz_last_game(json)
                with Session(self.dota_notes.database.engine) as session:
                    self.dota_notes.state.enrich_players_with_database(session)
                self.window.draw_match_with_state(self.dota_notes.state)
                self.on_select_player(0)
                self.window.draw_status_message("Found last game in Stratz history and updated UI.")
            else:
                self.window.draw_status_message(f"No last game found for specified user {steam_id.as_32}.")

    def is_valid_search(self, steam_id):
        """Check if there is work to do with the str specified by the user.

        Args:
            steam_id: str to use for the request
        """
        if steam_id == "" or not steam_id.isdigit():
            return False
        else:
            with Session(self.dota_notes.database.engine) as session:
                last_search = session.query(SettingEntity).filter_by(key="last_search").one_or_none()
                if last_search is not None:
                    last_search.value = steam_id
                else:
                    last_search = SettingEntity("last_search", steam_id)
                    session.add(last_search)
                session.commit()
            return True

    def on_stratz_info(self):
        """Use Stratz to look for player info (smurfs, games, pro names)"""
        if self.dota_notes.settings.stratz_token == "":
            return
        to_fetch = []
        for player in self.dota_notes.state.players:
            if player.steam_id != 0:
                to_fetch.append(player.steam_id)
        json = stratz_get_players_info(self.dota_notes.settings.stratz_token, to_fetch)
        if json is not None:
            self.dota_notes.state.enrich_players_with_stratz_info(json)
            self.window.draw_match_with_state(self.dota_notes.state)
            self.on_select_player(self.last_selected_index)
            self.window.draw_status_message("Updated player with Stratz info.")
        else:
            self.window.draw_status_message("Error while fetching player info from Stratz.")

    def on_save_player_details(self):
        """User press 'save' on the player detail page"""
        player_state = self.last_selected_player
        player_state.custom_name = self.window.inputDetailsCustomName.text()
        player_state.smurf = self.window.comboBoxDetailsSmurf.currentText()
        player_state.is_racist = self.window.checkBoxDetailsRacist.isChecked()
        player_state.is_sexist = self.window.checkBoxDetailsSexist.isChecked()
        player_state.is_toxic = self.window.checkBoxDetailsToxic.isChecked()
        player_state.is_feeder = self.window.checkBoxDetailsFeeder.isChecked()
        player_state.gives_up = self.window.checkBoxDetailsGivesUp.isChecked()
        player_state.destroys_items = self.window.checkBoxDetailsDestroysItems.isChecked()
        player_state.rages_buyback = self.window.checkBoxDetailsBuyback.isChecked()
        player_state.note = self.window.inputDetailsNote.toPlainText()
        self.window.draw_match_player(self.last_selected_index, player_state)
        with Session(self.dota_notes.database.engine) as session:
            player_info = session.get(PlayerEntity, str(player_state.steam_id))
            if player_info is None:
                player_info = PlayerEntity.make_from_state(player_state)
                session.add(player_info)
            else:
                player_info.name = player_state.name
                PlayerEntity.import_export(player_state, player_info)
            session.commit()
