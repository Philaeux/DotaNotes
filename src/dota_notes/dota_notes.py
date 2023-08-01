import multiprocessing
import sys

from dota_notes.data.application_state import ApplicationState
from dota_notes.data.database import Database, Setting
from dota_notes.app_flask import flask_process
from dota_notes.app_dota import dota_process
from dota_notes.ui.app_qt import QtApp

from sqlalchemy.orm import Session


class DotaNotes:
    def __init__(self):
        self.state = ApplicationState()

        self.match_information_from_gsi = multiprocessing.Queue()
        self.user_steam_id_to_dota = multiprocessing.Queue()
        self.server_id_from_dota = multiprocessing.Queue()
        self.database = Database()
        self.app_qt = QtApp(self)

        self.steam_api_key = ""

    def run(self):
        # Web Server
        app_flask = multiprocessing.Process(target=flask_process, args=(58765, self.match_information_from_gsi,))
        app_flask.start()

        # Dota client
        steam_username = ""
        steam_password = ""
        self.steam_api_key = ""
        with Session(self.database.engine) as session:
            row = session.get(Setting, "steam_user")
            if row is not None:
                steam_username = row.value
            row = session.get(Setting, "steam_password")
            if row is not None:
                steam_password = row.value
            row = session.get(Setting, "steam_api_key")
            if row is not None:
                self.steam_api_key = row.value

        app_dota = multiprocessing.Process(
            target=dota_process,
            args=(steam_username, steam_password, self.user_steam_id_to_dota, self.server_id_from_dota,)
        )
        app_dota.start()

        # Qt App
        return_code = self.app_qt.run()

        # Clean
        app_flask.kill()
        app_dota.kill()
        sys.exit(return_code)
