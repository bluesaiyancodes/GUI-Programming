# Step 5. C 버튼 — 두 번째 슬롯, 여러 칸을 차지하는 버튼
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
            button.clicked.connect(self.number_clicked)
            row = i // 3 + 1
            col = i % 3
            grid.addWidget(button, row, col)

        clear_button = QPushButton("C")
        clear_button.setFixedHeight(60)
        clear_button.clicked.connect(self.clear_display)
        grid.addWidget(clear_button, 4, 0, 2, 3)    # 4행, 3칸 차지

        self.setLayout(grid)

    # slot 1
    def number_clicked(self):
        digit = self.sender().text()
        print("clicked:", digit)
        current = self.display.text()
        if current == "0":
            self.display.setText(digit)
        else:
            self.display.setText(current + digit)

    # slot 2
    def clear_display(self):
        print("clear")
        self.display.setText("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
