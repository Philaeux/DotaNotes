from dota_notes.data.database import Setting


class Settings:

    gsi_port: int = 58765
    software_mode: str = "Client"
    proxy_url: str = "https://dota-notes.the-cluster.org"
    proxy_api_key: str = ""
    steam_user: str = ""
    steam_password: str = ""
    steam_api_key: str = ""

    TO_IMPORT_EXPORT = ["software_mode", "proxy_url", "proxy_api_key", "steam_user", "steam_password", "steam_api_key"]

    def import_from_database(self, session):

        for at in self.TO_IMPORT_EXPORT:
            row = session.get(Setting, at)
            if row is not None:
                setattr(self, at, row.value)
            else:
                session.add(Setting(at, getattr(self, at)))
