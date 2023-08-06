import os
import sys
from typing import Optional

from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped


class Database(object):
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
        self.uri = 'sqlite+pysqlite:///{0}/sqlite.db'.format(file_uri)
        self.engine = create_engine(self.uri, echo=False)
        BaseEntity.metadata.create_all(self.engine)

        with Session(self.engine) as session:
            if session.get(SettingEntity, "version") is None:
                session.add(SettingEntity("version", "1"))
            session.commit()


class BaseEntity(DeclarativeBase):
    """Database model base class"""
    pass


class SettingEntity(BaseEntity):
    """An application setting.

    Attributes:
        key: unique string defining a setting
        value: value of the setting
    """
    __tablename__ = 'settings'

    key: Mapped[str] = mapped_column(primary_key=True)
    value: Mapped[str] = mapped_column()

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"Setting(key={self.key!r}, value={self.value!r})"


class PlayerEntity(BaseEntity):
    """Player information

    Attributes:
        steam_id: unique identifier
        name: last seen name
        pro_name: pro name (if fetched from the API)
        custom_name: user set name
        smurf: user defined smurf indicator
        is_racist: flag
        is_sexist: flag
        is_toxic: flag
        is_feeder: flag
        gives_up: flag
        destroys_items: flag
        note: user set note
    """
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
        """Create an entity from its state counterpart

        Args:
            player_state: state to import information from
        """
        return PlayerEntity(
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
        """Copy the attributes from state to entity (or reverse)

        Args:
            from_object: Object to copy attributes from (can be entity or state)
            to_object: Object to copy attributes to (can be entity or state)
        """
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
        return f"Player(steam_id{self.steam_id!r}, last_seen_name={self.name!r}, custom_name={self.custom_name!r})"
