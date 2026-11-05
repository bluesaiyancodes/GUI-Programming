# Step 2. 표시창 + QGridLayout
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

        self.display = QLineEdit("0")
        self.display.setReadOnly(True)          # 키보드로 직접 못 고치게
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)

        grid = QGridLayout()
        # addWidget(위젯, 행, 열, 차지할 행 수, 차지할 열 수)
        grid.addWidget(self.display, 0, 0, 1, 3)
        self.setLayout(grid)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
