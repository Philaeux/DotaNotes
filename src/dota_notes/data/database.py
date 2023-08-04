import os
import sys
from select import select
from typing import Optional

from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped


class Database:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            file_uri = os.path.dirname(sys.executable)
        elif __file__:
            file_uri = os.path.dirname(__file__)
        self.uri = 'sqlite+pysqlite:///{0}/sqlite.db'.format(file_uri)
        self.engine = create_engine(self.uri, echo=False)
        Base.metadata.create_all(self.engine)

        with Session(self.engine) as session:
            if session.get(Setting, "version") is None:
                session.add(Setting("version", "1"))
            session.commit()


class Base(DeclarativeBase):
    pass


class Setting(Base):
    __tablename__ = 'settings'

    key: Mapped[str] = mapped_column(primary_key=True)
    value: Mapped[str] = mapped_column()

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"Setting(key={self.key!r}, value={self.value!r})"


class Player(Base):
    __tablename__ = 'players'

    steam_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    pro_name: Mapped[Optional[str]] = mapped_column()
    custom_name: Mapped[str] = mapped_column()
    smurf: Mapped[str] = mapped_column()
    is_racist: Mapped[bool] = mapped_column()
    is_sexist: Mapped[bool] = mapped_column()
    is_toxic: Mapped[bool] = mapped_column()
    is_feeder: Mapped[bool] = mapped_column()
    gives_up: Mapped[bool] = mapped_column()
    destroys_items: Mapped[bool] = mapped_column()
    note: Mapped[str] = mapped_column(String(500))

    def __init__(self, steam_id, name, pro_name=None, custom_name="", smurf="", is_racist=False, is_sexist=False,
                 is_toxic=False, is_feeder=False, gives_up=False, destroys_items=False, note=""):
        self.steam_id = steam_id
        self.name = name
        self.pro_name = pro_name
        self.custom_name = custom_name
        self.smurf = smurf
        self.is_racist = is_racist
        self.is_sexist = is_sexist
        self.is_toxic = is_toxic
        self.is_feeder = is_feeder
        self.gives_up = gives_up
        self.destroys_items = destroys_items
        self.note = note

    @staticmethod
    def make_from_state(player_state):
        return Player(
            str(player_state.steam_id),
            player_state.name,
            player_state.pro_name if player_state.pro_name != "" else None,
            player_state.custom_name,
            player_state.smurf,
            player_state.is_racist,
            player_state.is_sexist,
            player_state.is_toxic,
            player_state.is_feeder,
            player_state.gives_up,
            player_state.destroys_items)

    @staticmethod
    def import_export(from_object, to_object):
        to_object.pro_name = from_object.pro_name
        to_object.custom_name = from_object.custom_name
        to_object.smurf = from_object.smurf
        to_object.is_racist = from_object.is_racist
        to_object.is_sexist = from_object.is_sexist
        to_object.is_toxic = from_object.is_toxic
        to_object.is_feeder = from_object.is_feeder
        to_object.gives_up = from_object.gives_up
        to_object.destroys_items = from_object.destroys_items
        to_object.note = from_object.note

    def __repr__(self) -> str:
        return f"Player(steam_id{self.steam_id!r}, last_seen_name={self.name!r}, " \
               f"pro_name={self.pro_name!r}, custom_name={self.custom_name!r}, smurf={self.smurf!r})"
