from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = Signal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        self.clicked.emit(self.objectName(), self.text())
