import sys
from datetime import datetime

from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QFrame, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton

from sqlalchemy.orm import Session
from d2notes.data.database import Setting
from d2notes.helpers import get_game_live_stats


class QtApp:
    def __init__(self, d2notes):
        self.d2notes = d2notes

        # Build App
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setWindowTitle("Dota 2 Notes")

        # Menu
        menu = self.window.menuBar()
        file_menu = menu.addMenu("&File")
        self.status_message("Ready")
        settings_action = QAction("Settings", self.window)
        file_menu.addAction(settings_action)
        file_menu.addSeparator()
        exit_action = QAction("Exit", self.window)
        exit_action.triggered.connect(self.window.close)
        file_menu.addAction(exit_action)

        # Define pages
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)

        first_page_layout = QHBoxLayout()
        first_page_left_layout = QVBoxLayout()
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        divider.setMidLineWidth(1)
        first_page_right_layout = QVBoxLayout()
        first_page_layout.addLayout(first_page_left_layout)
        first_page_layout.addWidget(divider)
        first_page_layout.addLayout(first_page_right_layout)
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        divider.setMidLineWidth(1)
        central_layout.addLayout(first_page_layout)
        central_layout.addWidget(divider)

        # First Page Left Side
        # -Steam ID Selector
        first_line = QWidget()
        first_line_layout = QHBoxLayout()
        first_line.setLayout(first_line_layout)
        phil_button = QPushButton("Philaeux")
        first_line_layout.addWidget(phil_button)
        bububu_button = QPushButton("Bububu")
        first_line_layout.addWidget(bububu_button)
        grubby_button = QPushButton("Grubby")
        first_line_layout.addWidget(grubby_button)
        last_search_string = ""
        with Session(self.d2notes.database.engine) as session:
            last_search = session.get(Setting, "last_search")
            if last_search is not None:
                last_search_string = last_search.value
        self.steam_id_line = QLineEdit(last_search_string)
        phil_button.clicked.connect(lambda: self.steam_id_line.setText("76561197961298382"))
        bububu_button.clicked.connect(lambda: self.steam_id_line.setText("76561198066647717"))
        grubby_button.clicked.connect(lambda: self.steam_id_line.setText("76561198809738927"))
        first_line_layout.addWidget(self.steam_id_line)
        steam_compute_button = QPushButton("Search")
        steam_compute_button.clicked.connect(self.search_user_game)
        first_line_layout.addWidget(steam_compute_button)
        first_page_left_layout.addWidget(first_line)

        # -Match header display
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        divider.setMidLineWidth(1)
        first_page_left_layout.addWidget(divider)

        second_line = QWidget()
        second_line_layout = QHBoxLayout()
        second_line.setLayout(second_line_layout)
        label_match_id_title = QLabel("Match ID: ")
        second_line_layout.addWidget(label_match_id_title)
        self.label_match_id = QLabel("................")
        second_line_layout.addWidget(self.label_match_id)
        label_server_id_title = QLabel("Server ID: ")
        second_line_layout.addWidget(label_server_id_title)
        self.label_server_id = QLabel("................")
        second_line_layout.addWidget(self.label_server_id)
        first_page_left_layout.addWidget(second_line)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        divider.setMidLineWidth(1)
        first_page_left_layout.addWidget(divider)

        # -Player list display
        table_layout = QGridLayout()
        table_layout.setHorizontalSpacing(0)
        table_layout.setVerticalSpacing(0)
        column_width = [150, 150, 150, 150, 150, 150]
        headers = ["In-Game Name", "Pro Name", "Custom Name", "Games", "Languages", "Warnings"]

        # --Header
        for col in range(len(column_width)):
            cell = QLabel(headers[col])
            cell.setAlignment(Qt.AlignCenter)
            cell.setFixedSize(column_width[col], 60)
            table_layout.addWidget(cell, 0, col)
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setFrameShadow(QFrame.Shadow.Sunken)
        table_layout.addWidget(divider, 1, 0, 1, len(headers))

        # --Content
        self.match_player_labels = []
        for teams in range(2):
            for player in range(5):
                labels = []
                for col in range(len(column_width)):
                    cell = ClickableLabel(player, "")
                    cell.setAlignment(Qt.AlignCenter)
                    cell.clicked.connect(self.row_clicked)
                    cell.setFixedSize(column_width[col], 60)
                    table_layout.addWidget(cell, teams*6+player+2, col)
                    labels.append(cell)
                self.match_player_labels.append(labels)

            if teams == 0:
                divider = QFrame()
                divider.setFrameShape(QFrame.Shape.HLine)
                divider.setFrameShadow(QFrame.Shadow.Sunken)
                table_layout.addWidget(divider, 6*teams+7, 0, 1, len(headers))
        first_page_left_layout.addLayout(table_layout)

        # First Page right side
        test = QLabel("test")
        first_page_right_layout.addWidget(test)

        # Show main window
        self.window.setCentralWidget(central_widget)
        self.window.setGeometry(0, 0, 600, 400)
        self.window.show()

    def status_message(self, message, timeout=0):
        self.window.statusBar().showMessage(datetime.now().strftime("%H:%M:%S - ") + message, timeout)

    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.process_queues)
        timer.start(100)

        return_code = self.app.exec_()
        timer.stop()
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
                self.status_message("Found game info for player " + self.steam_id_line.text() + " using WEBAPI.")
                self.update_match_ui(self.d2notes.state)
            else:
                self.status_message("No game found for player " + self.steam_id_line.text())

    def open_settings(self):
        pass

    def row_clicked(self, row):
        print(row)

    def update_match_ui(self, data):
        self.label_match_id.setText(str(data.match_id))
        self.label_server_id.setText(str(data.server_id))
        for index, player in enumerate(data.players):
            self.match_player_labels[index][0].setText(player.name)
            self.match_player_labels[index][1].setText(player.pro_name)
            self.match_player_labels[index][2].setText(player.custom_name)

    def search_user_game(self):
        if self.steam_id_line.text() != "":
            self.d2notes.user_steam_id_to_dota.put(self.steam_id_line.text())
            session = self.d2notes.database.sessions()
            last_search = session.query(Setting).filter_by(key="last_search").one_or_none()
            if last_search is not None:
                last_search.value = self.steam_id_line.text()
            else:
                last_search = Setting("last_search", self.steam_id_line.text())
                session.add(last_search)
            session.commit()


# Custom label that emits a signal when clicked
class ClickableLabel(QLabel):
    clicked = Signal(int)

    def __init__(self, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row

    def mousePressEvent(self, event):
        self.clicked.emit(self.row)

