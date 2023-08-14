from dota_notes.data.models.settings_entity import SettingEntity


class Settings(object):
    """Singleton defining settings used by the application.

    Attributes:
        _instance: Singleton instance
        gsi_port: Port used by the http server awaiting request from GSI
        stratz_token: ...
    """

    _instance = None
    gsi_port: int = 58765
    stratz_token: str = ""

    TO_IMPORT_EXPORT = ["gsi_port", "stratz_token"]

    def __new__(cls, *args, **kwargs):
        """New overload to create a singleton."""
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def import_from_database(self, session):
        """Import this object attributes from the database.

        Args:
            session: Database session to use for requests
        """
        for at in self.TO_IMPORT_EXPORT:
            row = session.get(SettingEntity, at)
            if row is not None:
                at_type = type(getattr(self, at))
                if at_type is bool:
                    setattr(self, at, row.value == "True")
                else:
                    setattr(self, at, at_type(row.value))
            else:
                session.add(SettingEntity(at, str(getattr(self, at))))

    def export_to_database(self, session):
        """Export this object attributes to the database.

        Args:
            session: Database session to use for requests
        """
        for at in self.TO_IMPORT_EXPORT:
            row = session.get(SettingEntity, at)
            if row is not None:
                at_type = type(getattr(self, at))
                row.value = at_type(getattr(self, at))
            else:
                session.add(SettingEntity(at, str(getattr(self, at))))
