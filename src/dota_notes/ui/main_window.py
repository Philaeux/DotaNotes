from datetime import datetime

from PySide6.QtGui import QFontDatabase, QPixmap
from PySide6.QtWidgets import QMainWindow

from dota_notes.helpers import ISO_3166_COUNTRIES
from dota_notes.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Application main window that is seeded with the generated class from .ui file"""

    SMURF_CHOICES = ["", "Account Buyer", "Booster", "Main", "Maybe", "Smurf", "Sweaty Smurf"]
    FLAGS = ["Racist", "Sexist", "Toxic", "Feeder", "GivesUp", "Destroyer",  "Buyback", "BMPause", "ResumesPause"]
    MODE_CHOICES = ["Client"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QFontDatabase().addApplicationFont(":/fonts/Roboto-Medium.ttf")

        self.centralStackedWidget.setCurrentIndex(0)

        for smurf_choice in self.SMURF_CHOICES:
            self.comboBoxDetailsSmurf.addItem(smurf_choice)
        for mode_choice in self.MODE_CHOICES:
            self.comboBoxSettingsMode.addItem(mode_choice)
        self.draw_connection_status("Off", "Off")

        for i in range(10):
            for flag in self.FLAGS:
                getattr(self, f"labelPlayer{i}Flag{flag}").setVisible(False)
            getattr(self, f"labelPlayer{i}SmurfStratz").setVisible(False)
            getattr(self, f"labelPlayer{i}Note").setVisible(False)

    def draw_status_message(self, message, timeout=0):
        """Draw a bottom status message with a date in front"""
        self.statusBar().showMessage(datetime.now().strftime("%H:%M:%S - ") + message, timeout)

    def draw_connection_status(self, steam: str, dota: str):
        """Display the correct label corresponding to the connection status"""
        possible_status = ["On", "Try", "Off"]
        for client in ["Steam", "Dota"]:
            for status in possible_status:
                getattr(self, f"label{client}Con{status}").setVisible(False)
        if steam not in possible_status or dota not in possible_status:
            return
        getattr(self, f"labelSteamCon{steam}").setVisible(True)
        getattr(self, f"labelDotaCon{dota}").setVisible(True)

        if steam == "Off" and dota == "Off":
            self.buttonConnect.setVisible(True)
        else:
            self.buttonConnect.setVisible(False)

    def draw_match_with_state(self, data):
        """Draw a match info in the main widget"""
        self.labelMatchId.setText(str(data.match_id))
        self.labelServerId.setText(str(data.server_id))
        for index, player in enumerate(data.players):
            if index > 9:
                break
            self.draw_match_player(index, player)

    def draw_match_player(self, player_slot, player_data):
        """Draw the player information on the specific slot"""
        getattr(self, f"labelPlayer{player_slot}Name").setText(player_data.name)
        getattr(self, f"labelPlayer{player_slot}Level").setText(
            str(player_data.account_level) if player_data.account_level is not None else "")
        getattr(self, f"labelPlayer{player_slot}CustomName").setText(
            player_data.custom_name if player_data.custom_name is not None else "")
        if player_data.country_code == "":
            getattr(self, f"labelPlayer{player_slot}Country").setToolTip("")
            getattr(self, f"labelPlayer{player_slot}Country").setPixmap(QPixmap())
        else:
            getattr(self, f"labelPlayer{player_slot}Country").setToolTip(
                ISO_3166_COUNTRIES.get(player_data.country_code, ""))
            getattr(self, f"labelPlayer{player_slot}Country").setPixmap(
                QPixmap(f":/images/flags/{player_data.country_code.lower()}.svg"))
        if player_data.medal is None:
            getattr(self, f"labelPlayer{player_slot}Medal").setPixmap(QPixmap())
        else:
            getattr(self, f"labelPlayer{player_slot}Medal").setPixmap(QPixmap(f":/images/ranks/{player_data.medal}.png"))

        getattr(self, f"labelPlayer{player_slot}ProName").setText(
            player_data.pro_name if player_data.pro_name is not None else "")
        getattr(self, f"labelPlayer{player_slot}GameCount").setText(
            str(player_data.match_count) if player_data.match_count is not None else "")
        getattr(self, f"labelPlayer{player_slot}Smurf").setText(player_data.smurf)
        if player_data.smurf_stratz is not None and player_data.smurf_stratz != 0:
            getattr(self, f"labelPlayer{player_slot}SmurfStratz").setVisible(True)
            getattr(self, f"labelPlayer{player_slot}SmurfStratz").setText(str(player_data.smurf_stratz))
        else:
            getattr(self, f"labelPlayer{player_slot}SmurfStratz").setVisible(False)
            getattr(self, f"labelPlayer{player_slot}SmurfStratz").setText("")
        getattr(self, f"labelPlayer{player_slot}FlagRacist").setVisible(player_data.is_racist)
        getattr(self, f"labelPlayer{player_slot}FlagSexist").setVisible(player_data.is_sexist)
        getattr(self, f"labelPlayer{player_slot}FlagToxic").setVisible(player_data.is_toxic)
        getattr(self, f"labelPlayer{player_slot}FlagFeeder").setVisible(player_data.is_feeder)
        getattr(self, f"labelPlayer{player_slot}FlagGivesUp").setVisible(player_data.gives_up)
        getattr(self, f"labelPlayer{player_slot}FlagDestroyer").setVisible(player_data.destroys_items)
        getattr(self, f"labelPlayer{player_slot}FlagBuyback").setVisible(player_data.rages_buyback)
        getattr(self, f"labelPlayer{player_slot}FlagBMPause").setVisible(player_data.bm_pause)
        getattr(self, f"labelPlayer{player_slot}FlagResumesPause").setVisible(player_data.resumes_pause)
        getattr(self, f"labelPlayer{player_slot}Note").setVisible(len(player_data.note) > 0)

    def draw_details_with_player(self, player_state):
        """Draw the details section with a specified player.

        Args:
            player_state: player state to draw in the section
        """
        self.labelDetailsSteamId.setText(str(player_state.steam_id))
        self.labelDetailsName.setText(player_state.name)
        self.inputDetailsCustomName.setText(player_state.custom_name)
        self.labelDetailsProName.setText(
            player_state.pro_name if player_state.pro_name is not None else "")
        self.labelDetailsMatchCount.setText(str(player_state.match_count))
        self.labelDetailsSmurfStratz.setText(
            str(player_state.smurf_stratz) if player_state.smurf_stratz is not None else "")
        self.comboBoxDetailsSmurf.setCurrentText(player_state.smurf)
        self.checkBoxDetailsRacist.setChecked(player_state.is_racist)
        self.checkBoxDetailsSexist.setChecked(player_state.is_sexist)
        self.checkBoxDetailsToxic.setChecked(player_state.is_toxic)
        self.checkBoxDetailsFeeder.setChecked(player_state.is_feeder)
        self.checkBoxDetailsGivesUp.setChecked(player_state.gives_up)
        self.checkBoxDetailsDestroysItems.setChecked(player_state.destroys_items)
        self.checkBoxDetailsBuyback.setChecked(player_state.rages_buyback)
        self.checkBoxDetailsPauseWar.setChecked(player_state.bm_pause)
        self.checkBoxDetailsResumesPause.setChecked(player_state.resumes_pause)
        self.inputDetailsNote.setPlainText(player_state.note)
