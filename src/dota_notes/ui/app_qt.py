import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session

from dota_notes.data.models.settings_entity import SettingEntity
from dota_notes.data.models.player_entity import PlayerEntity
from dota_notes.data.messages import MessageGSI
from dota_notes.helpers import stratz_get_players_info, stratz_get_last_game, stratz_get_live_game
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
        self.window.buttonBububu.clicked.connect(lambda: self.window.inputSteamId.setText("106381989"))
        self.window.buttonBulldog.clicked.connect(lambda: self.window.inputSteamId.setText("92832630"))
        self.window.buttonGrubby.clicked.connect(lambda: self.window.inputSteamId.setText("849473199"))
        self.window.buttonPhilaeux.clicked.connect(lambda: self.window.inputSteamId.setText("1032654"))
        self.window.buttonS4.clicked.connect(lambda: self.window.inputSteamId.setText("41231571"))
        self.window.buttonSearchLive.clicked.connect(self.on_search_live_game)
        self.window.buttonSearchLast.clicked.connect(self.on_search_last_game)
        self.window.buttonStratz.clicked.connect(self.on_stratz_profiles_search)
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
        timer = QTimer()
        timer.timeout.connect(self.process_queues)
        timer.start(100)

        return_code = self.app.exec_()
        return return_code

    def process_queues(self):
        while not self.dota_notes.message_queue_qt.empty():
            message = self.dota_notes.message_queue_qt.get(block=False)
            if isinstance(message, MessageGSI):
                self.dota_notes.state.last_gsi_match_id = message.match_id
                self.window.draw_match_with_state(self.dota_notes.state)

    def on_open_settings(self):
        settings = self.dota_notes.settings
        self.window.lineEditStratzToken.setText(settings.stratz_token)
        self.window.centralStackedWidget.setCurrentIndex(1)

    def on_settings_save(self):
        settings = self.dota_notes.settings
        settings.stratz_token = self.window.lineEditStratzToken.text()
        with Session(self.dota_notes.database.engine) as session:
            settings.export_to_database(session)
            session.commit()
        self.window.centralStackedWidget.setCurrentIndex(0)

    def on_settings_cancel(self):
        self.window.centralStackedWidget.setCurrentIndex(0)

    def on_label_click(self, label_name, label_text):
        row = 0
        for char in label_name:
            if char.isdigit():
                row = int(char)
        self.on_select_player(row)

    def on_select_player(self, player_slot):
        self.lastIndexSelected = player_slot
        player_state = self.dota_notes.state.players[player_slot]
        self.window.draw_details_with_player(player_state)

    def on_search_live_game(self):
        """Get current game info for a player (if any)"""
        if self.dota_notes.state.last_gsi_match_id == 0:
            return
        json = stratz_get_live_game(self.dota_notes.settings.stratz_token, self.dota_notes.state.last_gsi_match_id)
        if json is not None:
            self.dota_notes.state.update_with_live_game(json)
            with Session(self.dota_notes.database.engine) as session:
                self.dota_notes.state.enrich_players_with_database(session)
            self.window.draw_match_with_state(self.dota_notes.state)
            self.on_select_player(0)
            self.window.draw_status_message("Found live game and updated UI")
        else:
            self.window.draw_status_message("No live game info to draw")

    def on_search_last_game(self):
        """Get last game info for a player (if public)"""
        if self.dota_notes.settings.stratz_token == "":
            return
        steam_id = self.window.inputSteamId.text()
        if self.is_valid_search(steam_id):
            json = stratz_get_last_game(self.dota_notes.settings.stratz_token, steam_id)
            if json is not None:
                self.dota_notes.state.update_with_last_game(json)
                with Session(self.dota_notes.database.engine) as session:
                    self.dota_notes.state.enrich_players_with_database(session)
                self.window.draw_match_with_state(self.dota_notes.state)
                self.on_select_player(0)
                self.window.draw_status_message("Found last game and updated UI")
            else:
                self.window.draw_status_message("No last game found for specified user")

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

    def on_stratz_profiles_search(self):
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
            self.on_select_player(self.lastIndexSelected)
            self.window.draw_status_message("Updated player with stratz info.")

    def on_save_player_details(self):
        player_state = self.dota_notes.state.players[self.lastIndexSelected]
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
