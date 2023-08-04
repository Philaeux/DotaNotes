import multiprocessing
import sys

from dota_notes.data.game_state import GameState
from dota_notes.data.database import Database, Setting
from dota_notes.app_flask import flask_process
from dota_notes.app_dota import dota_process
from dota_notes.data.settings import Settings
from dota_notes.ui.app_qt import QtApp

from sqlalchemy.orm import Session


class DotaNotes:
    def __init__(self):
        self.state = GameState()
        self.database = Database()
        self.settings = Settings()
        with Session(self.database.engine) as session:
            self.settings.import_from_database(session)
            session.commit()

        self.match_information_from_gsi = multiprocessing.Queue()
        self.message_queue_dota = multiprocessing.Queue()
        self.message_queue_qt = multiprocessing.Queue()
        self.app_qt = QtApp(self)

    def run(self):
        # Web Server
        app_flask = multiprocessing.Process(target=flask_process, args=(self.settings.gsi_port,
                                                                        self.match_information_from_gsi,))
        app_flask.start()

        # Dota client
        app_dota = multiprocessing.Process(
            target=dota_process,
            args=(self.settings.steam_user, self.settings.steam_password, self.message_queue_dota,
                  self.message_queue_qt,)
        )
        app_dota.start()

        # Qt App
        return_code = self.app_qt.run()

        # Clean
        app_flask.kill()
        app_dota.kill()
        sys.exit(return_code)
