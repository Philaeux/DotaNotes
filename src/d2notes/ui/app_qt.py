import sys
from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow


from sqlalchemy.orm import Session
from d2notes.data.database import Setting
from d2notes.helpers import get_game_live_stats

from d2notes.ui.main_window import Ui_MainWindow


class QtApp:
    def __init__(self, d2notes):
        self.d2notes = d2notes

        # Build App
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

        # Connect actions
        self.window.actionSettings.triggered.connect(lambda: print("TODO"))
        self.window.actionExit.triggered.connect(self.window.close)
        self.window.buttonPhilaeux.clicked.connect(lambda: self.window.inputSteamId.setText("76561197961298382"))
        self.window.buttonBububu.clicked.connect(lambda: self.window.inputSteamId.setText("76561198066647717"))
        self.window.buttonGrubby.clicked.connect(lambda: self.window.inputSteamId.setText("76561198809738927"))
        self.window.buttonSearch.clicked.connect(self.search_user_game)

        with Session(self.d2notes.database.engine) as session:
            last_search = session.get(Setting, "last_search")
            if last_search is not None:
                self.window.inputSteamId.setText(last_search.value)

        self.status_message("Ready")

        #
        # # -Player list display
        # table_layout = QGridLayout()
        # table_layout.setHorizontalSpacing(0)
        # table_layout.setVerticalSpacing(0)
        # column_width = [160, 160, 160, 160, 160, 160]
        # headers = ["In-Game Name", "Pro Name", "Custom Name", "Games", "Languages", "Warnings"]
        #
        # # --Header
        # for col in range(len(column_width)):
        #     cell = QLabel(headers[col])
        #     cell.setAlignment(Qt.AlignCenter)
        #     cell.setFixedSize(column_width[col], 60)
        #     table_layout.addWidget(cell, 0, col)
        # divider = QFrame()
        # divider.setFrameShape(QFrame.Shape.HLine)
        # divider.setFrameShadow(QFrame.Shadow.Sunken)
        # table_layout.addWidget(divider, 1, 0, 1, len(headers))
        #
        # # --Content
        # self.match_player_labels = []
        # for teams in range(2):
        #     for player in range(5):
        #         labels = []
        #         for col in range(len(column_width)):
        #             cell = ClickableLabel(teams * 5 + player, "")
        #             cell.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        #             cell.clicked.connect(self.select_row)
        #             cell.setFixedSize(column_width[col], 60)
        #             table_layout.addWidget(cell, teams*6+player+2, col)
        #             labels.append(cell)
        #         self.match_player_labels.append(labels)
        #
        #     if teams == 0:
        #         divider = QFrame()
        #         divider.setFrameShape(QFrame.Shape.HLine)
        #         divider.setFrameShadow(QFrame.Shadow.Sunken)
        #         table_layout.addWidget(divider, 6*teams+7, 0, 1, len(headers))
        # first_page_left_layout.addLayout(table_layout)
        #
        # # First Page right side
        # line_layout = QHBoxLayout()
        # title = QLabel("Steam ID")
        # title.setFixedSize(160, 60)
        # title.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        # line_layout.addWidget(title)
        # self.details_steam_id = QLabel("")
        # title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        # line_layout.addWidget(self.details_steam_id)
        # first_page_right_layout.addLayout(line_layout)
        #
        # line_layout = QHBoxLayout()
        # title = QLabel("Name")
        # title.setFixedSize(160, 60)
        # title.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        # line_layout.addWidget(title)
        # self.details_name = QLabel("")
        # title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        # line_layout.addWidget(self.details_name)
        # first_page_right_layout.addLayout(line_layout)
        #
        # # Show main window
        # self.window.setCentralWidget(central_widget)
        # self.window.setGeometry(0, 0, 600, 400)
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
                self.update_match_ui(self.d2notes.state)
        while not self.d2notes.server_id_from_dota.empty():
            server_id = self.d2notes.server_id_from_dota.get(block=False)
            if server_id != 0:
                self.d2notes.state.server_id = server_id
                game_json = get_game_live_stats(self.d2notes.steam_api_key, self.d2notes.state.server_id)
                self.d2notes.state.update_with_json(game_json)
                self.status_message("Found game info for player " + self.window.inputSteamId.text() + " using WEBAPI.")
                self.update_match_ui(self.d2notes.state)
            else:
                self.status_message("No game found for player " + self.window.inputSteamId.text())

    def open_settings(self):
        pass

    def select_row(self, row):
        self.details_steam_id.setText(str(self.d2notes.state.players[row].steam_id))
        self.details_name.setText(self.d2notes.state.players[row].name)
        print(row)

    def update_match_ui(self, data):
        self.window.labelMatchId.setText(str(data.match_id))
        self.window.labelServerId.setText(str(data.server_id))
        for index, player in enumerate(data.players):
            if index > 0:
                return
            getattr(self.window, f"labelPlayer{index}Name").setText(player.name)
            getattr(self.window, f"labelPlayer{index}ProName").setText(player.pro_name)
            getattr(self.window, f"labelPlayer{index}CustomName").setText(player.custom_name)
            getattr(self.window, f"labelPlayer{index}GameCount").setText("")

    def search_user_game(self):
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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

