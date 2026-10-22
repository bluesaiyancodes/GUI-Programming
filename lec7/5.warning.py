import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("5. Warning")
        button = QPushButton("Check Battery")
        button.clicked.connect(self.show_warning)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def show_warning(self):
        # warning: 주의 (노란 ! 아이콘) - 오류는 아니지만 조심해야 할 때
        QMessageBox.warning(self, "Warning", "Battery is low (10%).")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
