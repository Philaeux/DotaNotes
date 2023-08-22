from PySide6.QtCore import QObject


class PlayerState(QObject):
    """In memory information about a player. Attributes similar to the PlayerEntity"""
    steam_id = 0
    avatar = ""
    account_level = None
    medal = None
    country_code = ""
    name = ""
    pro_name = None
    custom_name = ""
    match_count = None
    smurf = ""
    smurf_stratz = None
    is_racist = False
    is_sexist = False
    is_toxic = False
    is_feeder = False
    gives_up = False
    destroys_items = False
    rages_buyback = False
    bm_pause = False
    resumes_pause = False
    note = ""

    ATTRIBUTES_FOR_COPY = ["steam_id", "avatar", "account_level", "medal", "country_code",
                           "pro_name", "custom_name", "match_count", "smurf", "smurf_stratz",
                           "is_racist", "is_sexist", "is_toxic", "is_feeder", "gives_up", "destroys_items",
                           "rages_buyback", "bm_pause", "resumes_pause", "note"]

    def copy_from(self, from_object):
        """Copy attributes from another object into this

        Args:
            from_object: source of the copy
        """
        for at in self.ATTRIBUTES_FOR_COPY:
            setattr(self, at, getattr(from_object, at))

    def enrich_with_stratz_account_info(self, account):
        """Enrich the state using Stratz json information
        
        Args
            account: steamAccount json return from Stratz
        """
        if "id" in account and account["id"] is not None:
            self.steam_id = account["id"]
        if "avatar" in account and account["avatar"] is not None:
            self.avatar = account["avatar"]
        if "dotaAccountLevel" in account and account["dotaAccountLevel"] is not None:
            self.account_level = account["dotaAccountLevel"]
        if "smurfFlag" in account and account["smurfFlag"] is not None:
            self.smurf_stratz = account["smurfFlag"]
        if "countryCode" in account and account["countryCode"] is not None:
            self.country_code = account["countryCode"]
        if "name" in account and account["name"] is not None:
            self.name = account["name"]
        else:
            self.name = "< HIDDEN ACCOUNT >"
        if "isAnonymous" in account and isinstance(account["isAnonymous"], bool) and account["isAnonymous"]:
            self.medal = 0

        if "proSteamAccount" in account and account["proSteamAccount"] is not None:
            pro_steam_account = account["proSteamAccount"]
            if "name" in pro_steam_account and pro_steam_account["name"] is not None:
                self.pro_name = pro_steam_account["name"]
