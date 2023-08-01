from PySide6.QtWidgets import QMainWindow

from d2notes.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBoxDetailsSmurf.addItem("")
        self.comboBoxDetailsSmurf.addItem("Account Buyer")
        self.comboBoxDetailsSmurf.addItem("Booster")
        self.comboBoxDetailsSmurf.addItem("Main")
        self.comboBoxDetailsSmurf.addItem("Maybe")
        self.comboBoxDetailsSmurf.addItem("Smurf")
        self.comboBoxDetailsSmurf.addItem("Sweaty Smurf")

        for i in range(10):
            getattr(self, f"labelPlayer{i}FlagRacist").setVisible(False)
            getattr(self, f"labelPlayer{i}FlagSexist").setVisible(False)
            getattr(self, f"labelPlayer{i}FlagToxic").setVisible(False)
            getattr(self, f"labelPlayer{i}FlagFeeder").setVisible(False)
            getattr(self, f"labelPlayer{i}FlagGivesUp").setVisible(False)
            getattr(self, f"labelPlayer{i}FlagDestroyer").setVisible(False)
