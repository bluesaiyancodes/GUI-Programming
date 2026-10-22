import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. Question v2")
        button = QPushButton("Close Document")
        button.clicked.connect(self.ask)
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def ask(self):
        # 추가: 버튼 3개 + 기본 버튼(Enter 를 누르면 선택됨)
        answer = QMessageBox.question(
            self, "Save?", "Save changes before closing?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel)   # 기본 버튼

        if answer == QMessageBox.StandardButton.Yes:
            self.label.setText("Saved and closed")
        elif answer == QMessageBox.StandardButton.No:
            self.label.setText("Closed without saving")
        else:
            self.label.setText("Cancelled")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
