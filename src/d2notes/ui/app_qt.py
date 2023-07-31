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
        self.window.buttonPhilaeux.clicked.connect(lambda: self.window.inputSteamId.setText("76561197961298382"))
        self.window.buttonBububu.clicked.connect(lambda: self.window.inputSteamId.setText("76561198066647717"))
        self.window.buttonGrubby.clicked.connect(lambda: self.window.inputSteamId.setText("76561198809738927"))
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
        while not self.d2notes.match_id_from_gsi.empty():
            match_id = self.d2notes.match_id_from_gsi.get(block=False)
            if self.d2notes.state.match_id != match_id and match_id != 0:
                self.d2notes.state.match_id = match_id
                self.status_message("Detected match id " + self.d2notes.state.match_id + " from GSI.")
                self.update_match_with_state(self.d2notes.state)
        while not self.d2notes.server_id_from_dota.empty():
            server_id = self.d2notes.server_id_from_dota.get(block=False)
            if server_id != 0:
                self.d2notes.state.server_id = server_id
                game_json = get_game_live_stats(self.d2notes.steam_api_key, self.d2notes.state.server_id)
                self.d2notes.state.update_with_json(game_json)
                self.status_message("Found game info for player " + self.window.inputSteamId.text() + " using WEBAPI.")
                self.update_match_with_state(self.d2notes.state)
                self.update_details_with_player(0)
            else:
                self.status_message("No game found for player " + self.window.inputSteamId.text())

    def on_open_settings(self):
        pass

    def on_label_click(self, label_name, label_text):
        row = 0
        for char in label_name:
            if char.isdigit():
                row = int(char)
        self.lastIndexSelected = row
        self.update_details_with_player(row)

    def update_details_with_player(self, player_slot):
        player_state = self.d2notes.state.players[player_slot]
        self.window.labelDetailsSteamId.setText(str(player_state.steam_id))
        self.window.labelDetailsName.setText(player_state.name)
        self.window.labelDetailsProName.setText(
            player_state.pro_name if player_state.pro_name is not None else "")
        self.window.inputDetailsCustomName.setText(
            player_state.custom_name if player_state.custom_name is not None else "")

    def update_match_with_state(self, data):
        self.window.labelMatchId.setText(str(data.match_id))
        self.window.labelServerId.setText(str(data.server_id))
        for index, player in enumerate(data.players):
            if index > 9:
                break
            self.update_match_with_player(index, player)

    def update_match_with_player(self, player_slot, player_data):
        getattr(self.window, f"labelPlayer{player_slot}Name").setText(player_data.name)
        getattr(self.window, f"labelPlayer{player_slot}ProName").setText(
            player_data.pro_name if player_data.pro_name is not None else "")
        getattr(self.window, f"labelPlayer{player_slot}CustomName").setText(
            player_data.custom_name if player_data.custom_name is not None else "")
        getattr(self.window, f"labelPlayer{player_slot}GameCount").setText("")

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

    def save_player_details(self):
        player_state = self.d2notes.state.players[self.lastIndexSelected]
        player_state.pro_name = \
            self.window.labelDetailsProName.text() if self.window.labelDetailsProName != "" else None
        player_state.custom_name = \
            self.window.inputDetailsCustomName.text() if self.window.inputDetailsCustomName.text() != "" else None
        self.update_match_with_player(self.lastIndexSelected, player_state)
        with Session(self.d2notes.database.engine) as session:
            player_info = session.get(Player, str(player_state.steam_id))
            if player_info is None:
                player_info = Player(
                    str(player_state.steam_id),
                    player_state.name,
                    player_state.pro_name if player_state.pro_name != "" else None,
                    player_state.custom_name if player_state.custom_name != "" else None
                )
                session.add(player_info)
            else:
                player_info.name = player_state.name
                player_info.pro_name = player_state.pro_name
                player_info.custom_name = player_state.custom_name
            session.commit()

