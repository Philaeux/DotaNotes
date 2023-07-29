import multiprocessing
import sys

from d2notes.data.application_state import ApplicationState
from d2notes.data.database import Database, Setting
from d2notes.app_flask import flask_process
from d2notes.app_dota import dota_process
from d2notes.ui.app_qt import QtApp


class D2Notes:
    def __init__(self):
        self.state = ApplicationState()

        self.match_id_from_gsi = multiprocessing.Queue()
        self.user_steam_id_to_dota = multiprocessing.Queue()
        self.server_id_from_dota = multiprocessing.Queue()
        self.database = Database()
        self.app_qt = QtApp(self)

        self.steam_api_key = ""

    def run(self):
        # Web Server
        app_flask = multiprocessing.Process(target=flask_process, args=(58765, self.match_id_from_gsi,))
        app_flask.start()

        # Dota client
        steam_username = self.database.sessions().query(Setting).filter_by(key="steam_user").one_or_none()
        steam_password = self.database.sessions().query(Setting).filter_by(key="steam_password").one_or_none()
        self.steam_api_key = self.database.sessions().query(Setting).filter_by(key="steam_api_key").one_or_none().value
        app_dota = multiprocessing.Process(
            target=dota_process,
            args=(steam_username.value, steam_password.value, self.user_steam_id_to_dota, self.server_id_from_dota,)
        )
        app_dota.start()

        # Qt App
        return_code = self.app_qt.app.exec_()

        # Clean
        app_flask.kill()
        app_dota.kill()
        sys.exit(return_code)
