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
