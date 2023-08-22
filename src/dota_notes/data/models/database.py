import os
import sys
from pathlib import Path

from alembic import command
from alembic.config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dota_notes.data.models.base_entity import BaseEntity
from dota_notes.data.models.player_entity import PlayerEntity
from dota_notes.data.models.settings_entity import SettingEntity


class Database:
    """Singleton defining database URI and unique ressources.

    Attributes:
        _instance: Singleton instance
        uri: database location
        engine: database connection used for session generation
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """New overload to create a singleton."""
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        """Defines all necessary ressources (URI & engine) and create database if necessary."""

        file_uri = ""
        alembic = ""
        migrations = ""

        if getattr(sys, 'frozen', False):
            file_uri = os.path.dirname(sys.executable)
            alembic = Path(file_uri) / "alembic.ini"
            migrations = Path(file_uri) / "alembic"
        elif __file__:
            file_uri = os.path.dirname(__file__)
            alembic = Path(file_uri) / ".." / ".." / ".." / "alembic.ini"
            migrations = Path(file_uri) / ".." / ".." / "alembic"
        self.uri = f"sqlite+pysqlite:///{file_uri}/sqlite.db"
        self.engine = create_engine(self.uri, echo=False)

        alembic_cfg = Config(alembic)
        alembic_cfg.set_main_option('script_location', str(migrations))
        alembic_cfg.set_main_option('sqlalchemy.url', self.uri)
        command.upgrade(alembic_cfg, 'head')
