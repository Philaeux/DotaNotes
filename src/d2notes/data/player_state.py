from PySide6.QtCore import QObject


class PlayerState(QObject):
    steam_id = 0
    name = ""
    pro_name = None
    custom_name = ""
    smurf = ""
    is_racist = False
    is_sexist = False
    is_toxic = False
    is_feeder = False
    gives_up = False
    destroys_items = False
    note = ""
