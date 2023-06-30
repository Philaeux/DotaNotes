import multiprocessing
import sys
from queue import Empty

from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal

from d2notes.database import Database, Setting
from d2notes.flask_app import flask_process
from d2notes.steam_app import steam_process
from d2notes.qt_app import QtApp


class D2Notes:
    def __init__(self):
        self.data = D2NotesData()
        self.match_id_from_gsi = multiprocessing.Queue()
        self.match_id_to_dota = multiprocessing.Queue()
        self.database = Database()
        self.qt_app = QtApp(self)

    def run(self):
        # Create all services

        # Start all services
        flask_app = multiprocessing.Process(target=flask_process, args=(self.match_id_from_gsi,))
        flask_app.start()
        steam_username = self.database.sessions().query(Setting).filter_by(key="steam_user").one_or_none()
        steam_password = self.database.sessions().query(Setting).filter_by(key="steam_password").one_or_none()
        steam_app = multiprocessing.Process(target=steam_process, args=(steam_username.value, steam_password.value, self.match_id_to_dota,))
        steam_app.start()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.process_queues)
        timer.start(100)

        self.qt_app.app.exec_()
        timer.stop()
        flask_app.kill()
        steam_app.kill()

    def process_queues(self):
        while not self.match_id_from_gsi.empty():
            match_id = self.match_id_from_gsi.get(block=False)
            if self.data.match_id != match_id:
                self.data.match_id = match_id
                self.qt_app.new_match_id()
                self.match_id_to_dota.put(match_id)
                print(match_id)


class D2NotesData(QObject):
    match_id = 0

    def __init__(self):
        super().__init__()
