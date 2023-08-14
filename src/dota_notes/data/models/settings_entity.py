from sqlalchemy.orm import Mapped, mapped_column

from dota_notes.data.models.base_entity import BaseEntity


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
