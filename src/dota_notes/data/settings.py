from dota_notes.data.models.settings_entity import SettingEntity


class Settings(object):
    """Singleton defining settings used by the application.

    Attributes:
        _instance: Singleton instance
        gsi_port: Port used by the http server awaiting request from GSI
        stratz_token: stratz auth bearer token
        steam_user: Steam username for the dota client
        steam_password: Steam password for the dota client
        steam_api_key: Steam WEB API key for the Steam WEB API
    """

    _instance = None
    gsi_port: int = 58765
    software_mode: str = "Client"
    stratz_token: str = ""
    steam_user: str = ""
    steam_password: str = ""
    steam_api_key: str = ""

    TO_IMPORT_EXPORT = ["gsi_port", "software_mode", "stratz_token", "steam_user", "steam_password", "steam_api_key"]

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
