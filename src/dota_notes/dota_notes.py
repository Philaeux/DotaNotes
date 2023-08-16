import multiprocessing
import sys

from dota_notes.app_dota import dota_process
from dota_notes.data.states.game_state import GameState
from dota_notes.data.models.database import Database
from dota_notes.app_flask import flask_process
from dota_notes.data.settings import Settings
from dota_notes.ui.app_qt import QtApp

from sqlalchemy.orm import Session

import logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


class DotaNotes:
    """Main software class

    Attributes:
        settings: settings
        database: database connection
        state: in-memory data state
        message_queue_dota: queue to send message to the dota process
        message_queue_qt: queue to send message to the qt process
        app_flask: Web server process listening to GSI
        app_dota: Dota client process
        app_qt: Qt process
        """
    def __init__(self):
        self.settings = Settings()
        self.database = Database()
        self.state = GameState()
        with Session(self.database.engine) as session:
            self.settings.import_from_database(session)
            session.commit()

        self.match_information_from_gsi = multiprocessing.Queue()
        self.message_queue_dota = multiprocessing.Queue()
        self.message_queue_qt = multiprocessing.Queue()

        self.app_flask = multiprocessing.Process(target=flask_process, args=(self.settings.gsi_port,
                                                                             self.message_queue_qt,))
        self.app_dota = multiprocessing.Process(target=dota_process, args=(self.message_queue_dota,
                                                                           self.message_queue_qt,))
        self.app_qt = QtApp(self)

    def run(self):
        """Run the software"""
        self.app_flask.start()
        self.app_dota.start()
        return_code = self.app_qt.run()

        self.app_flask.kill()
        self.app_dota.kill()
        sys.exit(return_code)
