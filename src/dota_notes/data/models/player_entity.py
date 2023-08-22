from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from dota_notes.data.models.base_entity import BaseEntity


class PlayerEntity(BaseEntity):
    """Player information

    Attributes:
        steam_id: unique identifier
        name: last seen name
        pro_name: pro name (if fetched from the API)
        custom_name: user set name
        match_count: number of games played by the user (set by stratz)
        smurf: user defined smurf indicator
        smurf_stratz: smurf flag (set by stratz)
        is_racist: flag
        is_sexist: flag
        is_toxic: flag
        is_feeder: flag
        gives_up: flag
        destroys_items: flag
        rages_buyback: flag
        bm_pause: flag
        resumes_pause: flag
        note: user set note
    """
    __tablename__ = 'players'

    steam_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    pro_name: Mapped[Optional[str]] = mapped_column()
    custom_name: Mapped[str] = mapped_column()
    match_count: Mapped[Optional[int]] = mapped_column()
    smurf: Mapped[str] = mapped_column()
    smurf_stratz: Mapped[Optional[int]] = mapped_column()
    is_racist: Mapped[bool] = mapped_column()
    is_sexist: Mapped[bool] = mapped_column()
    is_toxic: Mapped[bool] = mapped_column()
    is_feeder: Mapped[bool] = mapped_column()
    gives_up: Mapped[bool] = mapped_column()
    destroys_items: Mapped[bool] = mapped_column()
    rages_buyback: Mapped[bool] = mapped_column()
    bm_pause: Mapped[bool] = mapped_column()
    resumes_pause: Mapped[bool] = mapped_column()
    note: Mapped[str] = mapped_column(String(500))

    def __init__(self, steam_id, name, pro_name=None, custom_name="", match_count=None, smurf="", smurf_stratz=None,
                 is_racist=False, is_sexist=False, is_toxic=False, is_feeder=False, gives_up=False,
                 destroys_items=False, rages_buyback=False, bm_pause=False, resumes_pause=False, note=""):
        self.steam_id = steam_id
        self.name = name
        self.pro_name = pro_name
        self.custom_name = custom_name
        self.match_count = match_count
        self.smurf = smurf
        self.smurf_stratz = smurf_stratz
        self.is_racist = is_racist
        self.is_sexist = is_sexist
        self.is_toxic = is_toxic
        self.is_feeder = is_feeder
        self.gives_up = gives_up
        self.destroys_items = destroys_items
        self.rages_buyback = rages_buyback
        self.bm_pause = bm_pause
        self.resumes_pause = resumes_pause
        self.note = note

    @staticmethod
    def make_from_state(player_state):
        """Create an entity from its state counterpart

        Args:
            player_state: state to import information from
        """
        entity = PlayerEntity(str(player_state.steam_id), player_state.name)
        PlayerEntity.import_export(from_object=player_state, to_object=entity)
        return entity

    @staticmethod
    def import_export(from_object, to_object):
        """Copy the attributes from state to entity (or reverse)

        Args:
            from_object: Object to copy attributes from (can be entity or state)
            to_object: Object to copy attributes to (can be entity or state)
        """
        to_object.pro_name = from_object.pro_name
        to_object.custom_name = from_object.custom_name
        to_object.match_count = from_object.match_count
        to_object.smurf = from_object.smurf
        to_object.smurf_stratz = from_object.smurf_stratz
        to_object.is_racist = from_object.is_racist
        to_object.is_sexist = from_object.is_sexist
        to_object.is_toxic = from_object.is_toxic
        to_object.is_feeder = from_object.is_feeder
        to_object.gives_up = from_object.gives_up
        to_object.destroys_items = from_object.destroys_items
        to_object.rages_buyback = from_object.rages_buyback
        to_object.bm_pause = from_object.bm_pause
        to_object.resumes_pause = from_object.resumes_pause
        to_object.note = from_object.note

    def __repr__(self) -> str:
        return f"Player(steam_id{self.steam_id!r}, last_seen_name={self.name!r}, custom_name={self.custom_name!r})"
