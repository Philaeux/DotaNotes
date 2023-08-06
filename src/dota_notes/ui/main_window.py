from datetime import datetime

from PySide6.QtWidgets import QMainWindow

from dota_notes.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Application main window that is seeded with the generated class from .ui file"""

    SMURF_CHOICES = ["", "Account Buyer", "Booster", "Main", "Maybe", "Smurf", "Sweaty Smurf"]
    FLAGS = ["Racist", "Sexist", "Toxic", "Feeder", "GivesUp", "Destroyer"]
    MODE_CHOICES = ["Client", "Proxy"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.centralStackedWidget.setCurrentIndex(0)

        for smurf_choice in self.SMURF_CHOICES:
            self.comboBoxDetailsSmurf.addItem(smurf_choice)
        for mode_choice in self.MODE_CHOICES:
            self.comboBoxSettingsMode.addItem(mode_choice)
        self.comboBoxSettingsMode.currentTextChanged.connect(self.on_settings_mode_changed)

        for i in range(10):
            for flag in self.FLAGS:
                getattr(self, f"labelPlayer{i}Flag{flag}").setVisible(False)

        self.draw_connection_status("Off", "Off")

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
        getattr(self, f"labelPlayer{player_slot}ProName").setText(
            player_data.pro_name if player_data.pro_name is not None else "")
        getattr(self, f"labelPlayer{player_slot}CustomName").setText(
            player_data.custom_name if player_data.custom_name is not None else "")
        getattr(self, f"labelPlayer{player_slot}Smurf").setText(player_data.smurf)
        getattr(self, f"labelPlayer{player_slot}FlagRacist").setVisible(player_data.is_racist)
        getattr(self, f"labelPlayer{player_slot}FlagSexist").setVisible(player_data.is_sexist)
        getattr(self, f"labelPlayer{player_slot}FlagToxic").setVisible(player_data.is_toxic)
        getattr(self, f"labelPlayer{player_slot}FlagFeeder").setVisible(player_data.is_feeder)
        getattr(self, f"labelPlayer{player_slot}FlagGivesUp").setVisible(player_data.gives_up)
        getattr(self, f"labelPlayer{player_slot}FlagDestroyer").setVisible(player_data.destroys_items)

    def on_settings_mode_changed(self, new_current_text):
        """When the user select a new mode, modify the Settings UI accordingly"""
        if new_current_text == "Proxy":
            self.lineEditSettingsProxyURL.setEnabled(True)
            self.lineEditSettingsProxyAPIKey.setEnabled(True)
            self.lineEditSettingsSteamUser.setEnabled(False)
            self.lineEditSettingsSteamPassword.setEnabled(False)
            self.lineEditSettingsSteamAPIKey.setEnabled(False)
        elif new_current_text == "Client":
            self.lineEditSettingsProxyURL.setEnabled(False)
            self.lineEditSettingsProxyAPIKey.setEnabled(False)
            self.lineEditSettingsSteamUser.setEnabled(True)
            self.lineEditSettingsSteamPassword.setEnabled(True)
            self.lineEditSettingsSteamAPIKey.setEnabled(True)
