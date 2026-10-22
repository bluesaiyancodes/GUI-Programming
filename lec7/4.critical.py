import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("4. Critical")
        button = QPushButton("Open File")
        button.clicked.connect(self.show_error)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def show_error(self):
        # critical: 심각한 오류 (빨간 X 아이콘)
        QMessageBox.critical(self, "Error", "File not found!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
