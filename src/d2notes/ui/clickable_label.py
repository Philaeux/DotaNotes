from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = Signal(int)

    def __init__(self, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row

    def mousePressEvent(self, event):
        self.clicked.emit(self.row)
