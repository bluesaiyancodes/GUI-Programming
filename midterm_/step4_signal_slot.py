# Step 4. Signal & Slot — 버튼 9개를 슬롯 하나에 연결, sender()로 누른 버튼 찾기
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton,
                             QGridLayout)
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("보강 데모 - 계산기")
        self.setFixedSize(300, 360)

        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)

        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 3)

        numbers = ["7", "8", "9",
                   "4", "5", "6",
                   "1", "2", "3"]
        for i, text in enumerate(numbers):
            button = QPushButton(text)
            button.setFixedHeight(60)
            button.clicked.connect(self.number_clicked)   # signal -> slot
            row = i // 3 + 1
            col = i % 3
            grid.addWidget(button, row, col)

        self.setLayout(grid)

    # slot
    def number_clicked(self):
        digit = self.sender().text()        # 어떤 버튼이 시그널을 보냈나?
        print("clicked:", digit)
        current = self.display.text()
        if current == "0":
            self.display.setText(digit)
        else:
            self.display.setText(current + digit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
