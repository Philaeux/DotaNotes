from PySide6.QtWidgets import QMainWindow

from dota_notes.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    SMURF_CHOICES = ["", "Account Buyer", "Booster", "Main", "Maybe", "Smurf", "Sweaty Smurf"]
    FLAGS = ["Racist", "Sexist", "Feeder", "GivesUp", "Destroyer"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for smurf_choice in self.SMURF_CHOICES:
            self.comboBoxDetailsSmurf.addItem(smurf_choice)

        for i in range(10):
            for flag in self.FLAGS:
                getattr(self, f"labelPlayer{i}Flag{flag}").setVisible(False)

        for client in ["Steam", "Dota"]:
            for status in ["On", "Try", "Off"]:
                getattr(self, f"label{client}Con{status}").setVisible(False)
