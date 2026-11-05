# Step 3. 숫자 버튼 1~9 — for 문으로 행·열 계산
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
            row = i // 3 + 1      # 0행은 표시창이므로 1행부터
            col = i % 3
            grid.addWidget(button, row, col)

        self.setLayout(grid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
