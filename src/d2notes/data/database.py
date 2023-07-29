import os
import sys

from sqlalchemy import create_engine, inspect, Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Database:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            file_uri = os.path.dirname(sys.executable)
        elif __file__:
            file_uri = os.path.dirname(__file__)
        self.uri = 'sqlite:///{0}/sqlite.db'.format(file_uri)
        self.engine = create_engine(self.uri)
        self.sessions = sessionmaker(bind=self.engine)
        if not inspect(self.engine).has_table("settings"):
            Base.metadata.create_all(self.engine)
            session = self.sessions()
            session.add(Setting("version", "1"))
            session.add(Setting("steam_user", ""))
            session.add(Setting("steam_password", ""))
            session.add(Setting("steam_api_key", ""))
            session.commit()


class Setting(Base):
    __tablename__ = 'settings'

    key = Column(String, primary_key=True)
    value = Column(String)

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Player(Base):
    __tablename__ = 'player'

    id = Column(String, primary_key=True)
    custom_name = Column(String)
    pro_name = Column(String)
    history = Column(JSON)

    def __init(self, id):
        self.id = id
