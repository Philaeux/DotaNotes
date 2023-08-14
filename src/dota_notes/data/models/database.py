import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dota_notes.data.models.base_entity import BaseEntity
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
        if getattr(sys, 'frozen', False):
            file_uri = os.path.dirname(sys.executable)
        elif __file__:
            file_uri = os.path.dirname(__file__)
        self.uri = f"sqlite+pysqlite:///{file_uri}/sqlite.db"
        self.engine = create_engine(self.uri, echo=False)
        BaseEntity.metadata.create_all(self.engine)

        with Session(self.engine) as session:
            if session.get(SettingEntity, "version") is None:
                session.add(SettingEntity("version", "1"))
            session.commit()
