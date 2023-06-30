import sys

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton


class QtApp:
    def __init__(self, d2notes):
        self.d2notes = d2notes

        # Build App
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setWindowTitle("Dota 2 Notes")
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Build Content
        first_line = QWidget()
        first_line_layout = QHBoxLayout()
        first_line.setLayout(first_line_layout)
        self.label_match_id = QLabel("Waiting to detect a match id...")
        first_line_layout.addWidget(self.label_match_id)
        self.layout.addWidget(first_line)

        table_layout = QGridLayout()
        row_count = 10
        column_width = [150, 150, 150, 150, 150, 150]
        headers = ["In-Game Name", "Pro Name", "Custom Name", "Games", "Languages", "Warnings"]

        # Header
        for col in range(len(column_width)):
            cell = QLabel(headers[col])
            cell.setAlignment(Qt.AlignCenter)
            cell.setFixedSize(column_width[col], 60)
            table_layout.addWidget(cell, 0, col)

        # Content
        for row in range(1, row_count+1):
            for col in range(len(column_width)):
                cell = ClickableLabel(row, col, "Cell")
                cell.setAlignment(Qt.AlignCenter)
                cell.clicked.connect(self.cell_clicked)
                cell.setFixedSize(column_width[col], 60)
                table_layout.addWidget(cell, row, col)

        # Add table layout to main layout
        self.layout.addLayout(table_layout)

        # Show main window
        self.window.setCentralWidget(self.central_widget)
        self.window.setGeometry(0, 0, 600, 400)
        self.window.show()

    def run(self):
        sys.exit(self.app.exec_())

    def cell_clicked(self, row, col):
        print(row)

    def new_match_id(self):
        self.label_match_id.setText(str(self.d2notes.data.match_id))


# Custom label that emits a signal when clicked
class ClickableLabel(QLabel):
    clicked = Signal(int, int)

    def __init__(self, row, col, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col

    def mousePressEvent(self, event):
        self.clicked.emit(self.row, self.col)

