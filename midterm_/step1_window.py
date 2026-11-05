# Step 1. 빈 창 만들기 — QWidget을 상속한 클래스
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("보강 데모 - 계산기")
        self.setFixedSize(300, 360)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
