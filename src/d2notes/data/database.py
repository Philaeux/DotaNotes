import os
import sys
from select import select

from sqlalchemy import create_engine
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
            if session.query(Setting).filter_by(key="steam_user").one_or_none() is None:
                session.add(Setting("steam_user", ""))
            if session.query(Setting).filter_by(key="steam_password").one_or_none() is None:
                session.add(Setting("steam_password", ""))
            if session.query(Setting).filter_by(key="steam_api_key").one_or_none() is None:
                session.add(Setting("steam_api_key", ""))
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
    __tablename__ = 'player'

    steam_id: Mapped[str] = mapped_column(primary_key=True)
    last_seen_name: Mapped[str] = mapped_column()
    pro_name: Mapped[str] = mapped_column()
    custom_name: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Player(steam_id{self.steam_id!r}, last_seen_name={self.last_seen_name!r}, pro_name={self.pro_name!r}, custom_name={self.custom_name!r})"
