from PySide6.QtCore import QObject


class PlayerState(QObject):
    steam_id = 0
    name = ""
    pro_name = None
    custom_name = None
