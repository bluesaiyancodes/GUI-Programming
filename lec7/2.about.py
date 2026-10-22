import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2. About")
        button = QPushButton("About")
        button.clicked.connect(self.show_about)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def show_about(self):
        # about: 프로그램 소개 (버튼은 OK 하나, 아이콘은 프로그램 아이콘)
        QMessageBox.about(self, "About", "My First App\nVersion 1.0")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

