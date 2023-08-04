from PySide6.QtWidgets import QMainWindow

from dota_notes.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    SMURF_CHOICES = ["", "Account Buyer", "Booster", "Main", "Maybe", "Smurf", "Sweaty Smurf"]
    FLAGS = ["Racist", "Sexist", "Feeder", "GivesUp", "Destroyer"]
    MODE_CHOICES = ["Proxy Server", "Client"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.centralStackedWidget.setCurrentIndex(0)

        for smurf_choice in self.SMURF_CHOICES:
            self.comboBoxDetailsSmurf.addItem(smurf_choice)
        for mode_choice in self.MODE_CHOICES:
            self.comboBoxSettingsMode.addItem(mode_choice)

        for i in range(10):
            for flag in self.FLAGS:
                getattr(self, f"labelPlayer{i}Flag{flag}").setVisible(False)

        self.draw_connection_status("Off", "Off")

    def draw_connection_status(self, steam: str, dota: str):
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
